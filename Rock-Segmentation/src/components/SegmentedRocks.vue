<script lang="ts">
export default {
  data() {
    return {
      segmentedVideoUrl: 'http://127.0.0.1:5000/video/segmented',
    };
  },
};
</script>

<template>
  <div>
    <h2 class="title">
      Video Segmentado
    </h2>
    <img :src="segmentedVideoUrl" alt="Segmentation applied on the video" class="segmented"/>
  </div>
</template>


<style scoped>
.title{
  text-align:center;
}
</style>
