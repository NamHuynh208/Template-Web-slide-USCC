<script setup lang="ts">
defineProps<{ value: string; label: string; hint?: string }>()
</script>

<template>
  <div class="stat">
    <div class="value">{{ value }}</div>
    <div class="label">{{ label }}</div>
    <div v-if="hint" class="hint">{{ hint }}</div>
  </div>
</template>

<style scoped>
.stat { background: var(--c-bg-alt); border-radius: var(--radius); box-shadow: var(--shadow); padding: 28px 24px; text-align: center; }
.value { font-size: 2.6em; font-weight: 800; color: var(--c-primary); line-height: 1; }
.label { margin-top: 0.5em; font-weight: 600; }
.hint { margin-top: 0.3em; font-size: 0.8em; color: var(--c-muted); }
</style>
