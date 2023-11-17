import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {

  // 상태
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)

  // 객체
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
