<template>
    <div class="center">
        <h1>가수 정보 페이지에 오신 것을 환영합니다</h1>
        <p>여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</p>
        <img :src="microphone" alt="microphone image" class="img_width">
    </div>
</template>

<script setup>
import microphone from '@/assets/microphone.jpg'
</script>

<style scoped>
.img_width {
    width: 200px
}
.center {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center; /* 추가하여 텍스트도 중앙 정렬이 되도록 합니다 */
}

</style>