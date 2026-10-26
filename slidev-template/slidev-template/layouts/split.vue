<script setup lang="ts">
defineProps<{ image?: string; side?: 'left' | 'right' }>()
</script>

<template>
  <div class="split" :class="side === 'left' ? 'rev' : ''">
    <div class="text"><slot /></div>
    <div class="media" :style="image ? { backgroundImage: `url(${image})` } : {}">
      <div v-if="!image" class="placeholder">Thêm ảnh bằng <code>image: /anh.png</code></div>
    </div>
  </div>
</template>

<style scoped>
.split { display: grid; grid-template-columns: 1.1fr 1fr; width: 100%; height: 100%; background: var(--c-bg); }
.split.rev { direction: rtl; }
.split.rev > * { direction: ltr; }
.text { padding: var(--pad); display: flex; flex-direction: column; justify-content: center; }
.text :deep(h1) { font-size: 2em; margin: 0 0 0.6em; }
.media { background-size: cover; background-position: center; background-color: var(--c-primary-soft); display: grid; place-items: center; }
.placeholder { color: var(--c-primary); font-size: 0.9em; padding: 1em; text-align: center; }
</style>
