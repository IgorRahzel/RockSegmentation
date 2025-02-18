<script lang="ts">
export default {
  data() {
    return {
      segmentedVideoUrl: 'http://127.0.0.1:5000/video/mask', // Flask route for segmented video frames
    };
  },
};
</script>

<template>
  <div>
    <h2 class="title">
      Mascára
    </h2>
    <!-- Dynamically bind the segmented video URL to the src -->
    <img :src="segmentedVideoUrl" alt="Masked Segementation" class="masked"/>
  </div>
</template>

<style scoped>
.title{
  text-align: center;
}
  

</style>