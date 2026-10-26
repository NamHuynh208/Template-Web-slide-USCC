<script setup lang="ts">
defineProps<{ author?: string }>()
</script>

<template>
  <div class="quote">
    <div class="mark">“</div>
    <blockquote><slot /></blockquote>
    <p v-if="author" class="author">— {{ author }}</p>
  </div>
</template>

<style scoped>
.quote {
  width: 100%;
  height: 100%;
  padding: 0 calc(var(--pad) * 1.6);
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: var(--c-primary-soft);
  position: relative;
}
.mark { position: absolute; left: var(--pad); top: 40px; font-size: 10em; color: var(--c-primary); opacity: 0.2; line-height: 1; }
blockquote { font-size: 1.9em; font-weight: 600; line-height: 1.4; margin: 0; color: var(--c-text); }
blockquote :deep(p) { margin: 0; }
.author { margin-top: 1.2em; color: var(--c-primary); font-weight: 600; }
</style>
