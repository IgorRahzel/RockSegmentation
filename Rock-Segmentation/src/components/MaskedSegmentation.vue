<script lang="ts">
export default {
  data() {
    return {
      segmentedVideoUrl: 'http://127.0.0.1:5000/video/mask',
    };
  },
};
</script>

<template>
  <div>
    <h2 class="title">
      Mascára
    </h2>
    <img :src="segmentedVideoUrl" alt="Masked Segementation" class="masked"/>
  </div>
</template>

<style scoped>
.title{
  text-align: center;
}
  

</style>