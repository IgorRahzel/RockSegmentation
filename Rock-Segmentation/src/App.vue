<script lang="ts">
import MainComponent from './components/MainComponent.vue';

export default{
  components:{MainComponent}
}
</script>

<template>
  <MainComponent />
</template>

<style>
/* Global styles */
body {
  margin: 0;
  padding: 0;
  background: linear-gradient(to right, #01014d, #000011); /* Dark blue fading to darker */
  color: white; /* White text for contrast */
  font-family: Arial, sans-serif;
  min-height: 100vh; /* Ensure full height */
}
</style>
