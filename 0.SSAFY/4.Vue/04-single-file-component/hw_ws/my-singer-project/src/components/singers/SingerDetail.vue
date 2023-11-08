<template>
    <div class="card">
        <h1>가수 이름</h1>
        <img :src="singerIMG" alt="가수 이미지" class="singer-detail">
        <p>가수 소개글</p>
        <SingerAlbum />
        <SingerAlbum />
    </div>
</template>

<script setup>
import singerIMG from '@/assets/singer.jpg'
import SingerAlbum from '@/components/singers/SingerAlbum.vue'
</script>

<style scoped>
.singer-detail {
  width: 200px; /* 지름이 200px인 원으로 설정 */
  height: 200px; /* 지름이 200px인 원으로 설정 */
  border-radius: 50%; /* 이미지를 원형으로 만듭니다 */
}

</style>

<style>
/* h1 {
    color:greenyellow
} */
</style>