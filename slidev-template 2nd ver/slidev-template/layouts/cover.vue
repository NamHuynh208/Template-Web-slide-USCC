<script setup lang="ts">
defineProps<{ eyebrow?: string; note?: string }>()
</script>

<template>
  <div class="cover">
    <div class="bg-sweep" aria-hidden="true"></div>
    <div class="bg-wave" aria-hidden="true"></div>
    <div class="cover-logo"><img src="/uscc-logo.png" alt="USCC — HCMUS Chess Club" /></div>
    <div class="university">
      TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN<br /><b>Câu lạc bộ Cờ - USCC</b>
    </div>
    <div class="cover-copy">
      <div v-if="eyebrow" class="eyebrow">{{ eyebrow }}</div>
      <slot />
    </div>
    <small v-if="note" class="cover-note">{{ note }}</small>
    <span class="page-num">{{ ($slidev.nav.page < 10 ? '0' : '') + $slidev.nav.page }}</span>
  </div>
</template>

<style scoped>
.cover {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: linear-gradient(67deg, #ffffff 2%, #f4f4f4 99%);
  color: var(--c-navy);
}

.bg-sweep {
  position: absolute;
  inset: 0;
  background: url('/sweep-navy.svg') center / 100% 100% no-repeat;
  opacity: 0.22;
  pointer-events: none;
}

.bg-wave {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 24%;
  background: url('/wave-gold.svg') center bottom / 100% 100% no-repeat;
  pointer-events: none;
}

.cover-logo { position: absolute; z-index: 2; top: 40px; left: 84px; width: 190px; }
.cover-logo img { display: block; width: 100%; }

.university {
  position: absolute;
  z-index: 2;
  right: 102px;
  top: 45px;
  text-align: center;
  color: var(--c-university);
  font-size: 15px;
  line-height: 1.8;
}

.university b { font-size: 1.35em; }

.cover-copy { position: absolute; z-index: 2; left: 85px; top: 187px; width: 691px; }

.cover-note {
  position: absolute;
  z-index: 2;
  left: 85px;
  top: 461px;
  color: var(--c-blue);
  font-size: 10px;
}
</style>
