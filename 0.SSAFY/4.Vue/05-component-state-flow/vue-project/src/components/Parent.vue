<template>
  <div>
    <ParentChild 
      my-msg="message" 
      :dynamic-props="name" 
      @some-event="someCallback"
    />
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
import { ref } from 'vue'

const name = ref('Alice')
const someCallback = function () {
  console.log('ParentChild가 발신한 emit 이벤트를 수신했습니다~!')
}
</script>

<style scoped>

</style>
