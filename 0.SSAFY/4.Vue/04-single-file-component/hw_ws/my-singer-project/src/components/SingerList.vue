<template>
    <div class="center">
        <h1 class="orangered">가수 목록</h1>
        <SingerDetail v-for="singer in singers"
        :key="singer.name"
        :singer="singer"/>
    </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue'
const singers = [{name: 'adele'}, {name: 'maroon 5'}, {name: 'Dua Lipa'}]
</script>

<style scoped>

div {
    margin-top: 50px;
    text-align: center;
}

.card {
    display: inline-block;
    width: 40%;
    margin: 20px;
    border: 2px solid rgb(90, 89, 89);
}

.orangered {
    color:orangered;
}

</style>