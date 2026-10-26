<script setup lang="ts">
defineProps<{ image?: string; side?: 'left' | 'right'; eyebrow?: string }>()
</script>

<template>
  <div class="split" :class="side === 'left' ? 'image-left' : 'image-right'">
    <div class="bg-sweep" aria-hidden="true"></div>
    <div class="bg-wave" aria-hidden="true"></div>
    <header>
      <span v-if="eyebrow" class="eyebrow">{{ eyebrow }}</span>
      <img src="/uscc-logo.png" alt="USCC — HCMUS Chess Club" />
    </header>
    <div class="content split-body">
      <div class="text"><slot /></div>
      <figure v-if="image" class="figure">
        <img :src="image" alt="" />
      </figure>
    </div>
    <span class="page-num">{{ ($slidev.nav.page < 10 ? '0' : '') + $slidev.nav.page }}</span>
  </div>
</template>

<style scoped>
.split {
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

.split-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 44px;
  align-items: start;
}

.image-left .split-body .text { order: 2; }
.image-left .split-body .figure { order: 1; }

.figure { margin: 0; display: flex; justify-content: center; }

.figure img { max-width: 100%; max-height: 420px; object-fit: contain; }
</style>
