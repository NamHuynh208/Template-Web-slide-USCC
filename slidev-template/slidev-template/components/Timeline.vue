<script setup lang="ts">
defineProps<{ items: { title: string; desc?: string; time?: string }[] }>()
</script>

<template>
  <div class="timeline">
    <div v-for="(it, i) in items" :key="i" class="step">
      <div class="dot">{{ i + 1 }}</div>
      <div>
        <div class="t">{{ it.title }} <span v-if="it.time" class="chip">{{ it.time }}</span></div>
        <div v-if="it.desc" class="d">{{ it.desc }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.timeline { display: flex; flex-direction: column; gap: 18px; }
.step { display: flex; gap: 16px; align-items: flex-start; }
.dot { flex: none; width: 36px; height: 36px; border-radius: 50%; background: var(--c-primary); color: #fff; display: grid; place-items: center; font-weight: 700; }
.t { font-weight: 700; font-size: 1.1em; }
.d { color: var(--c-muted); font-size: 0.9em; margin-top: 0.2em; }
</style>
