<template>
  <div class="content-slide">
    <div class="bar" />
    <div class="inner"><slot /></div>
    <div class="footer">
      <span>{{ $slidev.configs.title }}</span>
      <span>{{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}</span>
    </div>
  </div>
</template>

<style scoped>
.content-slide {
  position: relative;
  width: 100%;
  height: 100%;
  background: var(--c-bg);
  padding: 56px var(--pad) 64px;
}
.bar {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 8px;
  background: linear-gradient(90deg, var(--c-primary), var(--c-accent));
}
.inner :deep(h1) { font-size: 2em; margin: 0 0 0.6em; }
.footer {
  position: absolute;
  left: var(--pad);
  right: var(--pad);
  bottom: 20px;
  display: flex;
  justify-content: space-between;
  font-size: 0.7em;
  color: var(--c-muted);
}
</style>
