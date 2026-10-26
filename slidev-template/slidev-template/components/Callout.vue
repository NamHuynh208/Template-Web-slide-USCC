<script setup lang="ts">
defineProps<{ type?: 'info' | 'tip' | 'warn'; title?: string }>()
</script>

<template>
  <div class="callout" :class="type || 'info'">
    <strong v-if="title">{{ title }}</strong>
    <div><slot /></div>
  </div>
</template>

<style scoped>
.callout { border-left: 6px solid var(--c-primary); background: var(--c-primary-soft); border-radius: var(--radius-sm); padding: 16px 20px; margin: 1em 0; }
.callout strong { display: block; margin-bottom: 0.3em; }
.tip { border-color: #10b981; background: #ecfdf5; }
.warn { border-color: var(--c-accent); background: #fffbeb; }
</style>
