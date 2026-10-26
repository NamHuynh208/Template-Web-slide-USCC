#!/usr/bin/env python3
"""
Inspect a PowerPoint .pptx/.potx as an OOXML template source.

This script automates the mechanical parts of frontend-slides convert-template:
- open the file as a ZIP archive
- enumerate slides, slide masters, slide layouts, themes, and media
- parse common drawable XML elements: p:sp, p:pic, p:graphicFrame, p:cxnSp, p:grpSp
- extract text, geometry, fills, lines, font runs, placeholders, and image relationships
- resolve .rels targets to ppt/media/*
- copy media into a controlled output folder for later semantic renaming
- emit a JSON inventory that an LLM/human can use to write preview.md/design.md

It does NOT infer visual grammar or asset roles. Those remain design interpretation.
"""

from __future__ import annotations

import argparse
import json
import posixpath
import shutil
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}

R_EMBED = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
R_LINK = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}link"

EMU_PER_INCH = 914400
PX_PER_INCH = 96


def emu_to_px(value: Optional[int]) -> Optional[float]:
    if value is None:
        return None
    return round(value / EMU_PER_INCH * PX_PER_INCH, 3)


def sort_ooxml_paths(paths: Iterable[str]) -> List[str]:
    def key(path: str) -> Tuple[str, int, str]:
        stem = Path(path).stem
        digits = "".join(ch for ch in stem if ch.isdigit())
        return (posixpath.dirname(path), int(digits or 0), path)

    return sorted(paths, key=key)


def xml_root(zf: zipfile.ZipFile, path: str) -> ET.Element:
    return ET.fromstring(zf.read(path))


def has_path(zf: zipfile.ZipFile, path: str) -> bool:
    return path in zf.namelist()


def rels_path_for(part_path: str) -> str:
    dirname = posixpath.dirname(part_path)
    basename = posixpath.basename(part_path)
    return posixpath.join(dirname, "_rels", basename + ".rels")


def normalize_part_target(base_part: str, target: str) -> str:
    if target.startswith("/"):
        return target.lstrip("/")
    return posixpath.normpath(posixpath.join(posixpath.dirname(base_part), target))


def load_rels(zf: zipfile.ZipFile, part_path: str) -> Dict[str, Dict[str, Any]]:
    path = rels_path_for(part_path)
    if not has_path(zf, path):
        return {}
    root = xml_root(zf, path)
    out: Dict[str, Dict[str, Any]] = {}
    for rel in root.findall("rel:Relationship", NS):
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if not rid or not target:
            continue
        mode = rel.attrib.get("TargetMode")
        resolved = target if mode == "External" else normalize_part_target(part_path, target)
        out[rid] = {
            "id": rid,
            "type": rel.attrib.get("Type"),
            "target": target,
            "target_mode": mode,
            "resolved": resolved,
        }
    return out


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def get_text(el: ET.Element) -> str:
    parts = []
    for t in el.findall(".//a:t", NS):
        if t.text:
            parts.append(t.text)
    return "".join(parts).strip()


def get_shape_name(el: ET.Element) -> Optional[str]:
    c_nv_pr = el.find(".//p:cNvPr", NS)
    if c_nv_pr is not None:
        return c_nv_pr.attrib.get("name")
    return None


def get_placeholder(el: ET.Element) -> Optional[Dict[str, Any]]:
    ph = el.find(".//p:ph", NS)
    if ph is None:
        return None
    return dict(ph.attrib)


def get_xfrm(el: ET.Element, slide_size: Optional[Dict[str, int]] = None) -> Optional[Dict[str, Any]]:
    xfrm = el.find(".//a:xfrm", NS)
    if xfrm is None:
        return None
    off = xfrm.find("a:off", NS)
    ext = xfrm.find("a:ext", NS)

    x = int(off.attrib.get("x", 0)) if off is not None else None
    y = int(off.attrib.get("y", 0)) if off is not None else None
    w = int(ext.attrib.get("cx", 0)) if ext is not None else None
    h = int(ext.attrib.get("cy", 0)) if ext is not None else None

    box: Dict[str, Any] = {
        "emu": {"x": x, "y": y, "w": w, "h": h},
        "px96": {"x": emu_to_px(x), "y": emu_to_px(y), "w": emu_to_px(w), "h": emu_to_px(h)},
    }

    if slide_size and slide_size.get("cx") and slide_size.get("cy"):
        cx = slide_size["cx"]
        cy = slide_size["cy"]
        box["stage1920"] = {
            "x": round((x or 0) / cx * 1920, 2),
            "y": round((y or 0) / cy * 1080, 2),
            "w": round((w or 0) / cx * 1920, 2),
            "h": round((h or 0) / cy * 1080, 2),
        }
    return box


def srgb_from_scheme(root: ET.Element) -> Dict[str, str]:
    scheme: Dict[str, str] = {}
    clr_scheme = root.find(".//a:clrScheme", NS)
    if clr_scheme is None:
        return scheme
    for child in list(clr_scheme):
        name = local_name(child.tag)
        srgb = child.find(".//a:srgbClr", NS)
        sysclr = child.find(".//a:sysClr", NS)
        if srgb is not None and "val" in srgb.attrib:
            scheme[name] = "#" + srgb.attrib["val"]
        elif sysclr is not None and "lastClr" in sysclr.attrib:
            scheme[name] = "#" + sysclr.attrib["lastClr"]
    return scheme


def color_value(color_el: Optional[ET.Element]) -> Optional[Dict[str, Any]]:
    if color_el is None:
        return None
    srgb = color_el.find("a:srgbClr", NS)
    if srgb is not None:
        return {"type": "srgb", "value": "#" + srgb.attrib.get("val", "")}
    scheme = color_el.find("a:schemeClr", NS)
    if scheme is not None:
        return {"type": "scheme", "value": scheme.attrib.get("val")}
    prst = color_el.find("a:prstClr", NS)
    if prst is not None:
        return {"type": "preset", "value": prst.attrib.get("val")}
    sysclr = color_el.find("a:sysClr", NS)
    if sysclr is not None:
        return {"type": "system", "value": sysclr.attrib.get("lastClr")}
    return None


def get_fill(el: ET.Element) -> Optional[Dict[str, Any]]:
    # Prefer direct shape properties where possible.
    sp_pr = el.find("p:spPr", NS) or el.find("p:grpSpPr", NS)
    if sp_pr is None:
        sp_pr = el.find(".//p:spPr", NS)
    if sp_pr is None:
        return None

    solid = sp_pr.find("a:solidFill", NS)
    if solid is not None:
        return {"kind": "solid", "color": color_value(solid)}
    grad = sp_pr.find("a:gradFill", NS)
    if grad is not None:
        stops = []
        for gs in grad.findall(".//a:gs", NS):
            stops.append({"pos": gs.attrib.get("pos"), "color": color_value(gs)})
        return {"kind": "gradient", "stops": stops}
    blip = sp_pr.find("a:blipFill", NS)
    if blip is not None:
        return {"kind": "image"}
    if sp_pr.find("a:noFill", NS) is not None:
        return {"kind": "none"}
    return None


def get_line(el: ET.Element) -> Optional[Dict[str, Any]]:
    ln = el.find(".//p:spPr/a:ln", NS)
    if ln is None:
        return None
    out: Dict[str, Any] = {"width_emu": int(ln.attrib.get("w", 0)) if "w" in ln.attrib else None}
    solid = ln.find("a:solidFill", NS)
    if solid is not None:
        out["color"] = color_value(solid)
    if ln.find("a:noFill", NS) is not None:
        out["color"] = {"kind": "none"}
    return out


def get_geometry(el: ET.Element) -> Optional[str]:
    prst = el.find(".//p:spPr/a:prstGeom", NS)
    if prst is not None:
        return prst.attrib.get("prst")
    cust = el.find(".//p:spPr/a:custGeom", NS)
    if cust is not None:
        return "custom"
    return None


def get_text_runs(el: ET.Element) -> List[Dict[str, Any]]:
    runs: List[Dict[str, Any]] = []
    for r in el.findall(".//a:r", NS):
        text = "".join(t.text or "" for t in r.findall("a:t", NS))
        rpr = r.find("a:rPr", NS)
        run: Dict[str, Any] = {"text": text}
        if rpr is not None:
            if "sz" in rpr.attrib:
                run["size_pt"] = int(rpr.attrib["sz"]) / 100
            if "b" in rpr.attrib:
                run["bold"] = rpr.attrib["b"] in ("1", "true")
            if "i" in rpr.attrib:
                run["italic"] = rpr.attrib["i"] in ("1", "true")
            latin = rpr.find("a:latin", NS)
            if latin is not None and "typeface" in latin.attrib:
                run["font"] = latin.attrib["typeface"]
            solid = rpr.find("a:solidFill", NS)
            if solid is not None:
                run["color"] = color_value(solid)
        runs.append(run)
    return runs


def get_picture_info(pic: ET.Element, rels: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    blip = pic.find(".//a:blip", NS)
    rid = None
    link = None
    if blip is not None:
        rid = blip.attrib.get(R_EMBED)
        link = blip.attrib.get(R_LINK)
    rel = rels.get(rid) if rid else None
    return {
        "rid": rid,
        "link_rid": link,
        "relationship": rel,
    }


def parse_element(el: ET.Element, kind: str, slide_size: Optional[Dict[str, int]], rels: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    item: Dict[str, Any] = {
        "kind": kind,
        "name": get_shape_name(el),
        "placeholder": get_placeholder(el),
        "box": get_xfrm(el, slide_size),
    }
    if kind == "shape":
        item.update({
            "text": get_text(el),
            "text_runs": get_text_runs(el),
            "geometry": get_geometry(el),
            "fill": get_fill(el),
            "line": get_line(el),
        })
    elif kind == "picture":
        item.update(get_picture_info(el, rels))
        item["fill"] = get_fill(el)
    elif kind == "graphicFrame":
        item["text"] = get_text(el)
        # Common embedded chart/table hints.
        uri_nodes = [node.attrib.get("uri") for node in el.findall(".//a:graphicData", NS)]
        item["graphic_uris"] = [u for u in uri_nodes if u]
    else:
        item["text"] = get_text(el)
        item["fill"] = get_fill(el)
        item["line"] = get_line(el)
    return item


def parse_part(zf: zipfile.ZipFile, path: str, slide_size: Optional[Dict[str, int]]) -> Dict[str, Any]:
    root = xml_root(zf, path)
    rels = load_rels(zf, path)
    elements: List[Dict[str, Any]] = []

    # Preserve broad XML order by scanning common containers recursively.
    for el in root.iter():
        tag = local_name(el.tag)
        if tag == "sp" and el.find("p:nvSpPr", NS) is not None:
            elements.append(parse_element(el, "shape", slide_size, rels))
        elif tag == "pic" and el.find("p:nvPicPr", NS) is not None:
            elements.append(parse_element(el, "picture", slide_size, rels))
        elif tag == "graphicFrame" and el.find("p:nvGraphicFramePr", NS) is not None:
            elements.append(parse_element(el, "graphicFrame", slide_size, rels))
        elif tag == "cxnSp" and el.find("p:nvCxnSpPr", NS) is not None:
            elements.append(parse_element(el, "connector", slide_size, rels))
        elif tag == "grpSp" and el.find("p:nvGrpSpPr", NS) is not None:
            elements.append(parse_element(el, "group", slide_size, rels))

    return {
        "path": path,
        "relationships": rels,
        "element_count": len(elements),
        "elements": elements,
    }


def parse_presentation(zf: zipfile.ZipFile) -> Dict[str, Any]:
    path = "ppt/presentation.xml"
    if not has_path(zf, path):
        return {}
    root = xml_root(zf, path)
    sld_sz = root.find("p:sldSz", NS)
    out: Dict[str, Any] = {"path": path}
    if sld_sz is not None:
        out["slide_size"] = {
            "cx": int(sld_sz.attrib.get("cx", 0)),
            "cy": int(sld_sz.attrib.get("cy", 0)),
            "type": sld_sz.attrib.get("type"),
        }
        out["slide_size"]["px96"] = {
            "w": emu_to_px(out["slide_size"]["cx"]),
            "h": emu_to_px(out["slide_size"]["cy"]),
        }
    return out


def parse_theme(zf: zipfile.ZipFile, path: str) -> Dict[str, Any]:
    root = xml_root(zf, path)
    major_fonts = []
    minor_fonts = []
    for node in root.findall(".//a:majorFont//a:latin", NS):
        if "typeface" in node.attrib:
            major_fonts.append(node.attrib["typeface"])
    for node in root.findall(".//a:minorFont//a:latin", NS):
        if "typeface" in node.attrib:
            minor_fonts.append(node.attrib["typeface"])
    return {
        "path": path,
        "name": root.attrib.get("name"),
        "colors": srgb_from_scheme(root),
        "major_fonts": sorted(set(major_fonts)),
        "minor_fonts": sorted(set(minor_fonts)),
    }


def copy_media(zf: zipfile.ZipFile, media_paths: List[str], out_assets: Path) -> List[Dict[str, str]]:
    out_assets.mkdir(parents=True, exist_ok=True)
    copied = []
    for media in media_paths:
        if not media.startswith("ppt/media/"):
            continue
        name = posixpath.basename(media)
        dest = out_assets / name
        with zf.open(media) as src, dest.open("wb") as dst:
            shutil.copyfileobj(src, dst)
        copied.append({"source": media, "copied_to": str(dest)})
    return copied


def collect_media_refs(parts: List[Dict[str, Any]]) -> Counter:
    refs: Counter = Counter()
    for part in parts:
        for el in part.get("elements", []):
            rel = el.get("relationship")
            if rel and rel.get("resolved"):
                refs[rel["resolved"]] += 1
    return refs


def summarize(elements_parts: List[Dict[str, Any]], themes: List[Dict[str, Any]], all_media: List[str], media_refs: Counter) -> Dict[str, Any]:
    kind_counts: Counter = Counter()
    placeholder_counts: Counter = Counter()
    font_counts: Counter = Counter()
    fill_counts: Counter = Counter()
    text_samples = []

    for part in elements_parts:
        for el in part.get("elements", []):
            kind_counts[el.get("kind")] += 1
            ph = el.get("placeholder")
            if ph:
                placeholder_counts[ph.get("type", "unknown")] += 1
            text = el.get("text")
            if text and len(text_samples) < 30:
                text_samples.append({"part": part["path"], "text": text[:160]})
            for run in el.get("text_runs", []) or []:
                if run.get("font"):
                    font_counts[run["font"]] += 1
            fill = el.get("fill")
            if fill:
                val = json.dumps(fill, sort_keys=True)
                fill_counts[val] += 1

    theme_colors = {}
    theme_fonts = set()
    for theme in themes:
        theme_colors.update(theme.get("colors", {}))
        theme_fonts.update(theme.get("major_fonts", []))
        theme_fonts.update(theme.get("minor_fonts", []))

    return {
        "element_kind_counts": dict(kind_counts),
        "placeholder_counts": dict(placeholder_counts),
        "fonts_seen_in_runs": dict(font_counts.most_common()),
        "theme_fonts": sorted(theme_fonts),
        "theme_colors": theme_colors,
        "most_common_fills": [json.loads(k) | {"count": v} for k, v in fill_counts.most_common(20)],
        "media_file_count": len(all_media),
        "referenced_media": dict(media_refs.most_common()),
        "unreferenced_media": sorted(set(all_media) - set(media_refs.keys())),
        "text_samples": text_samples,
    }


def inspect_pptx(input_path: Path, output_dir: Path) -> Dict[str, Any]:
    with zipfile.ZipFile(input_path) as zf:
        names = zf.namelist()
        presentation = parse_presentation(zf)
        slide_size = presentation.get("slide_size")

        slide_paths = sort_ooxml_paths(n for n in names if n.startswith("ppt/slides/slide") and n.endswith(".xml"))
        master_paths = sort_ooxml_paths(n for n in names if n.startswith("ppt/slideMasters/slideMaster") and n.endswith(".xml"))
        layout_paths = sort_ooxml_paths(n for n in names if n.startswith("ppt/slideLayouts/slideLayout") and n.endswith(".xml"))
        theme_paths = sort_ooxml_paths(n for n in names if n.startswith("ppt/theme/theme") and n.endswith(".xml"))
        media_paths = sorted(n for n in names if n.startswith("ppt/media/") and not n.endswith("/"))

        slides = [parse_part(zf, p, slide_size) for p in slide_paths]
        masters = [parse_part(zf, p, slide_size) for p in master_paths]
        layouts = [parse_part(zf, p, slide_size) for p in layout_paths]
        themes = [parse_theme(zf, p) for p in theme_paths]

        all_parts = slides + masters + layouts
        media_refs = collect_media_refs(all_parts)
        copied = copy_media(zf, media_paths, output_dir / "media")

        report = {
            "input": str(input_path),
            "package_counts": {
                "slides": len(slides),
                "slide_masters": len(masters),
                "slide_layouts": len(layouts),
                "themes": len(themes),
                "media": len(media_paths),
            },
            "presentation": presentation,
            "slides": slides,
            "slide_masters": masters,
            "slide_layouts": layouts,
            "themes": themes,
            "media": [{"path": p, "copied_to": str(output_dir / "media" / posixpath.basename(p))} for p in media_paths],
            "copied_media": copied,
        }
        report["summary"] = summarize(all_parts, themes, media_paths, media_refs)
        return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect PPTX/POTX template OOXML and emit JSON inventory.")
    parser.add_argument("input", help="Path to .pptx or .potx file")
    parser.add_argument("output_dir", nargs="?", default="pptx-template-inspect", help="Output directory")
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    report = inspect_pptx(input_path, output_dir)
    report_path = output_dir / "template-inspection.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    summary_path = output_dir / "summary.json"
    summary_path.write_text(json.dumps(report["summary"], indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {summary_path}")
    print("Package counts:", json.dumps(report["package_counts"], ensure_ascii=False))
    print("Referenced media:", len(report["summary"]["referenced_media"]))
    print("Copied media files:", len(report["copied_media"]))


if __name__ == "__main__":
    main()
