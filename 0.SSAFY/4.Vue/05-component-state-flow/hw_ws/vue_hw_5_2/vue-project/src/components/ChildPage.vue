<template>
    <div>
        <h3>자식 페이지입니다.</h3>
        <p>이름 : {{ childData.name }}</p>
        <p>나이 : {{ childData.age }}</p>
    </div>
</template>

<script setup>

defineProps({
    childData: Object
})
</script>

<style scoped>
h3 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

p {
  color: #34495e;
  margin: 0.25rem 0;
}
</style>
