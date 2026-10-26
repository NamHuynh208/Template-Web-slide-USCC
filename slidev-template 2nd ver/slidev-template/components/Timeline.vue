<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  items: Array<{ title: string; desc?: string; time?: string }>
}>()

const cols = computed(() => Math.min(Math.max(props.items?.length ?? 1, 1), 4))
</script>

<template>
  <div class="timeline">
    <article v-for="(item, i) in items" :key="i">
      <b>{{ String(i + 1).padStart(2, '0') }}</b>
      <h3 v-if="item.time" class="time">{{ item.time }}</h3>
      <h3>{{ item.title }}</h3>
      <p v-if="item.desc">{{ item.desc }}</p>
    </article>
  </div>
</template>

<style scoped>
.timeline {
  display: grid;
  grid-template-columns: repeat(v-bind(cols), 1fr);
  gap: 44px;
}

.timeline article {
  border-top: 2px solid var(--c-gold);
  padding-top: 16px;
}

.timeline b {
  display: block;
  margin-bottom: 18px;
  font-size: 44px;
  font-weight: 700;
  line-height: 1;
  color: var(--c-navy);
}

.timeline h3 { margin: 0 0 8px; font-size: 25px; font-weight: 700; line-height: 1.2; color: var(--c-navy); }

.timeline h3.time { margin: 0 0 10px; font-size: 11px; letter-spacing: 0.15em; color: var(--c-blue); }

.timeline p { margin: 0; font-size: 17px; line-height: 1.45; color: var(--c-blue); }
</style>
