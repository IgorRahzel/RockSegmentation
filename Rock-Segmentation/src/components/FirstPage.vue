<script lang="ts">
import MainButton from './MainButton.vue';

export default{
    components: {MainButton},
    data(){
        return{
            changePage: false
        };
    },
    methods:{
        GoToSecondPage(){
            this.changePage = true;
            this.$emit('SecondPage')
        }
    }
}
</script>

<template>
    <img src="/src/assets/cropped-TCX-FUNDO_TRANSP.webp" alt="TCX_logo" class="logo">
    <MainButton txt="Visualizar Esteira" @click="GoToSecondPage()" class="buttonFirstPage" />
</template>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center; /* Centers horizontally */
  justify-content: center;
  height: 100vh; /* Full screen height */
  position: relative;
}

.logo {
  max-width: 80%; /* Adjust size as needed */
  position: relative;
  top: -10%; /* Moves it up */
  margin-left: 50%; /* Moves it to the right */
}

.buttonFirstPage{
    position: relative;
    left: 60%; /* Moves it to the right */
    top: -30%; /* Moves it up */
}
</style>