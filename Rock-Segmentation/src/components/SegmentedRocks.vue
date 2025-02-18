<script lang="ts">
export default {
  data() {
    return {
      segmentedVideoUrl: 'http://127.0.0.1:5000/video/segmented', // Flask route for segmented video frames
    };
  },
};
</script>

<template>
  <div>
    <h2 class="title">
      Video Segmentado
    </h2>
    <!-- Dynamically bind the segmented video URL to the src -->
    <img :src="segmentedVideoUrl" alt="Segmentation applied on the video" class="segmented"/>
  </div>
</template>


<style scoped>
.title{
  text-align:center;
}
</style>
