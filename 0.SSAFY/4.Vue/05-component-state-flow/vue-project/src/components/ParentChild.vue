<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild :my-msg="myMsg" />
    <button @click="$emit('someEvent')">클릭</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue';

// 1. 문자열 배열 선언 방식
// defineProps(['myMsg'])

// 2. 객체 선언 방식
// defineProps({
//   myMsg: String,
// })

// props 데이터를 script에서 사용하려면
const props = defineProps({
                myMsg: String,
                dynamicProps: String,    // -> 유효성 검증
              })

console.log(props)
console.log(props.myMsg)

</script>

<style scoped>

</style>
