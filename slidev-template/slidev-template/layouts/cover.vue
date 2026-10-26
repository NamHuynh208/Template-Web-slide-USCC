<script setup lang="ts">
defineProps<{ subtitle?: string; author?: string; date?: string }>()
</script>

<template>
  <div class="cover">
    <div class="blob b1" />
    <div class="blob b2" />
    <div class="content">
      <span v-if="date" class="chip">{{ date }}</span>
      <div class="title"><slot /></div>
      <p v-if="subtitle" class="subtitle">{{ subtitle }}</p>
      <p v-if="author" class="author">{{ author }}</p>
    </div>
  </div>
</template>

<style scoped>
.cover {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: linear-gradient(135deg, var(--c-dark), #1e1b4b);
  color: #fff;
  display: flex;
  align-items: center;
  padding: var(--pad);
}
.blob { position: absolute; border-radius: 50%; filter: blur(60px); opacity: 0.55; }
.b1 { width: 420px; height: 420px; background: var(--c-primary); right: -80px; top: -100px; }
.b2 { width: 300px; height: 300px; background: var(--c-accent); right: 160px; bottom: -120px; opacity: 0.35; }
.content { position: relative; max-width: 70%; }
.title :deep(h1) { color: #fff; font-size: 3.2em; line-height: 1.1; margin: 0.4em 0 0.2em; }
.subtitle { font-size: 1.3em; color: #cbd5e1; margin: 0.4em 0 0; }
.author { margin-top: 2.5em; font-size: 0.95em; color: var(--c-accent); font-weight: 600; }
.chip { background: rgba(255, 255, 255, 0.12); color: #fff; }
</style>
