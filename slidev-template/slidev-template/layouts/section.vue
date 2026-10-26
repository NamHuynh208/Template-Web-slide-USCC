<script setup lang="ts">
defineProps<{ number?: string | number }>()
</script>

<template>
  <div class="section">
    <div v-if="number" class="num">{{ String(number).padStart(2, '0') }}</div>
    <div class="body"><slot /></div>
  </div>
</template>

<style scoped>
.section {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  gap: 48px;
  padding: var(--pad);
  background: var(--c-primary);
  color: #fff;
}
.num {
  font-size: 9em;
  font-weight: 800;
  line-height: 1;
  color: rgba(255, 255, 255, 0.25);
  font-family: var(--f-heading);
}
.body :deep(h1) { color: #fff; font-size: 2.8em; margin: 0; }
.body :deep(p) { color: #e0e7ff; font-size: 1.2em; margin-top: 0.6em; }
</style>
