<script setup lang="ts">
defineProps<{ eyebrow?: string }>()
</script>

<template>
  <div class="body-slide">
    <div class="bg-sweep" aria-hidden="true"></div>
    <div class="bg-wave" aria-hidden="true"></div>
    <header>
      <span v-if="eyebrow" class="eyebrow">{{ eyebrow }}</span>
      <img src="/uscc-logo.png" alt="USCC — HCMUS Chess Club" />
    </header>
    <div class="content">
      <slot />
    </div>
    <span class="page-num">{{ ($slidev.nav.page < 10 ? '0' : '') + $slidev.nav.page }}</span>
  </div>
</template>

<style scoped>
.body-slide {
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
  opacity: 0.28;
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

header {
  position: absolute;
  z-index: 2;
  top: 43px;
  left: 85px;
  right: 85px;
  height: 72px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

header img { width: 190px; height: 100%; object-fit: contain; }

.content { position: absolute; z-index: 2; top: 144px; left: 85px; right: 85px; }
</style>
