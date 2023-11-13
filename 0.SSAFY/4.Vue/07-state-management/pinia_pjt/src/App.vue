<template>
  <div></div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

console.log(store.count)

</script>

<style scoped>
</style>
