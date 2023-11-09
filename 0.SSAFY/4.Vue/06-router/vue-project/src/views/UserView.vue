<template>
    <div>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }} 유저의 페이지 입니다.</h2>
    <h2>{{ UserId }} 유저의 페이지 입니다.</h2>
    <button @click="goHome">홈으로!</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute, onBeforeRouteLeave } from 'vue-router'

const route = useRoute()
const UserId = ref(route.params.id)

// 프로그래밍 방식 네비게이션
const router = useRouter()

const goHome = function () {
    // router.push({ name: 'home' })
    router.replace({ name: 'home' })
}

// In-component Guard
// 1. onBeforeRouterLeave
onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('Are you sure you want to leave this page?')
    if (answer === false) {
        return false
    }
})


</script>

<style scoped>

</style>