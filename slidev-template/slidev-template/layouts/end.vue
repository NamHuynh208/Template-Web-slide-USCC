<script setup lang="ts">
defineProps<{ contact?: string }>()
</script>

<template>
  <div class="end">
    <div class="body"><slot /></div>
    <p v-if="contact" class="contact">{{ contact }}</p>
  </div>
</template>

<style scoped>
.end {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: linear-gradient(135deg, var(--c-dark), #1e1b4b);
  color: #fff;
}
.body :deep(h1) { color: #fff; font-size: 3.4em; margin: 0; }
.body :deep(p) { color: #cbd5e1; font-size: 1.2em; }
.contact { margin-top: 2em; color: var(--c-accent); font-weight: 600; }
</style>
