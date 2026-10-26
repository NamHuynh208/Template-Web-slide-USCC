<script setup lang="ts">
defineProps<{ eyebrow?: string }>()
</script>

<template>
  <div class="section">
    <div class="bg-sweep" aria-hidden="true"></div>
    <div class="bg-wave" aria-hidden="true"></div>
    <img class="center-logo" src="/uscc-logo.png" alt="USCC — HCMUS Chess Club" />
    <div v-if="eyebrow" class="centered-eyebrow eyebrow">{{ eyebrow }}</div>
    <div class="center-copy">
      <slot />
    </div>
    <span class="page-num">{{ ($slidev.nav.page < 10 ? '0' : '') + $slidev.nav.page }}</span>
  </div>
</template>

<style scoped>
.section {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: linear-gradient(67deg, #ffffff 2%, #f4f4f4 99%);
  color: var(--c-navy);
  text-align: center;
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

.center-logo { position: absolute; top: 47px; left: 50%; transform: translateX(-50%); width: 190px; }

.centered-eyebrow { position: absolute; top: 202px; width: 100%; z-index: 2; }

.center-copy {
  position: absolute;
  top: 238px;
  width: 100%;
  z-index: 2;
}

.center-copy :deep(.lead) { position: absolute; top: 165px; width: 100%; }
</style>
