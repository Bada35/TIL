<!--
    3-a. 사용자가 값을 입력할 수 있도록 input 태그를 작성한다.
    3-b. '입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.' 문구를 포함한 p 태그를 작성한다.
    3-c. 각각 글씨 색이 red, blue, green이 되도록 설정된 클래스 .red, .blue, .green을 style에 작성한다.
    3-d. 사용자가 입력한 값이 colorClass 변수에 할당 될 수 있도록 양방향 바인딩 directive를 사용한다.
    3-e colorClass 변수의 값이 첫 번째 p 태그의 class가 될 수 있도록 단방향 바인딩 directive를 사용한다.
-->

<template>
    <div>
        <input type="text" v-model="colorClass">
        <p :class="colorClass">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
    </div>
</template>

<script setup>
    import { ref } from 'vue'

    const colorClass = ref('')
</script>

<style>
.red {
    color: red;
}

.blue {
    color: blue;
}

.green {
    color: green;
}

</style>