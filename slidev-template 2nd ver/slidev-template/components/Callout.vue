<script setup lang="ts">
defineProps<{ title?: string }>()
</script>

<template>
  <aside class="callout">
    <strong v-if="title">{{ title }}</strong>
    <div class="callout-body"><slot /></div>
  </aside>
</template>

<style scoped>
.callout {
  margin-top: 28px;
  padding: 18px 24px;
  border-left: 4px solid var(--c-gold);
  background: rgba(241, 191, 12, 0.08);
  border-radius: 0 12px 12px 0;
}

.callout strong {
  display: block;
  margin-bottom: 6px;
  font-size: 17px;
  font-weight: 700;
  color: var(--c-navy);
  letter-spacing: 0.04em;
}

.callout-body { font-size: 17px; line-height: 1.45; color: var(--c-blue); }
</style>
