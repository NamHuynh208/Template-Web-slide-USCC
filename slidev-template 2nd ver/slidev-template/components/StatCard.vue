<script setup lang="ts">
defineProps<{
  value: string
  label: string
  progress?: number
  color?: 'gold' | 'navy' | 'blue'
}>()
</script>

<template>
  <article class="stat-card">
    <b>{{ value }}</b>
    <p>{{ label }}</p>
    <i
      v-if="progress !== undefined"
      :style="{ width: progress + '%', background: `var(--c-${color || 'gold'})` }"
      aria-hidden="true"
    ></i>
  </article>
</template>

<style scoped>
.stat-card {
  border-top: 2px solid var(--c-gold);
  padding-top: 16px;
}

.stat-card b {
  display: block;
  margin-bottom: 18px;
  font-size: 44px;
  font-weight: 700;
  line-height: 1;
  color: var(--c-navy);
}

.stat-card p { margin: 0; font-size: 17px; line-height: 1.45; color: var(--c-blue); }

.stat-card i {
  display: block;
  height: 8px;
  margin-top: 26px;
  border-radius: 5px;
  box-shadow: 60px 0 var(--c-track);
}
</style>
