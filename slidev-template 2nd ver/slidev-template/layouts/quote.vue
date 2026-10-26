<script setup lang="ts">
defineProps<{ author?: string }>()
</script>

<template>
  <div class="quote">
    <div class="bg-sweep" aria-hidden="true"></div>
    <div class="bg-wave" aria-hidden="true"></div>
    <div class="quote-body">
      <slot />
      <p v-if="author" class="author">— {{ author }}</p>
    </div>
    <span class="page-num">{{ ($slidev.nav.page < 10 ? '0' : '') + $slidev.nav.page }}</span>
  </div>
</template>

<style scoped>
.quote {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: linear-gradient(67deg, #ffffff 2%, #f4f4f4 99%);
  color: var(--c-navy);
  display: flex;
  align-items: center;
  justify-content: center;
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

.quote-body {
  position: relative;
  z-index: 2;
  max-width: 900px;
  padding: 0 60px;
}

.quote-body :deep(h1) {
  font-size: 46px;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.03em;
  color: var(--c-gold);
}

.author { margin-top: 28px; font-size: 20px; color: var(--c-blue); }
</style>
