<template>
    <div>
        <h1>부모 페이지입니다.</h1>
        <ChildPage v-for="child in children" :key="child.name" :child-data="child" />
    </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue'

const children = [
    { name: '김하나', age: 30, balance: 100000 },
    { name: '김두리', age: 20, balance: 10000 },
    { name: '김서이', age: 10, balance: 1000 }
]
</script>

<style scoped>
h1 {
  color: #1abc9c;
  margin-bottom: 1rem;
}

</style>


