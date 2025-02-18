<script lang="ts">
import Area from './Area.vue';
import FirstPage from './FirstPage.vue';
import MainButton from './MainButton.vue';
import MaskedSegmentation from './MaskedSegmentation.vue';
import SegmentedRocks from './SegmentedRocks.vue';

export default {
  components: {
    MaskedSegmentation,
    SegmentedRocks,
    FirstPage,
    MainButton,
    Area
  },
  data() {
    return {
      atFirstPage: true,
      currentTime: new Date().toLocaleTimeString()
    };
  },
  methods: {
    handlePageChange() {
      this.atFirstPage = !this.atFirstPage; // Hide FirstPage and show videos
    },
    updateTime() {
      this.currentTime = new Date().toLocaleTimeString(); // Atualiza o horário a cada segundo
    }
  },
  created() {
    setInterval(this.updateTime, 1000); // Atualiza o horário a cada segundo
  }
};
</script>

<template>
  <div v-if="atFirstPage">
    <FirstPage @SecondPage="handlePageChange" />
  </div>

  <div v-else>
    <div class="time-display">{{ currentTime }}</div>
    <img src="/src/assets/cropped-TCX-FUNDO_TRANSP.webp" alt="TCX_logo" class="logo">
    <h1 class="title">Pedras Segmentadas</h1>
    
    <div class="segmented-video">
      <SegmentedRocks class="segmentation"/>
    </div>

    <div class="masked-video">
      <MaskedSegmentation/>
    </div>

    <div class="area-display">
      <Area />
    </div>

    <MainButton txt="Sair" @click="handlePageChange" class="ExitButton"/>
  </div>
</template>


<style scoped>
.title {
  font-size: 3rem; /* Large text */
  color: #FFFAF3; /* Cream color */
  text-align: center; /* Center the text horizontally */
  font-weight: bold; /* Make it bold */
  position: absolute; /* Absolute positioning to place it at the top */
  top: 0px; /* Adjust the distance from the top */
  left: 50%; /* Center horizontally */
  transform: translateX(-50%); /* Fine-tunes the centering */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* Optional: Add shadow for effect */
}

.time-display {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 1.5rem;
  color: #FFFAF3;
  font-weight: bold;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
}

.logo {
  position: absolute;
  top: -25px;
  left: 0px;
  max-width: 10%;

}


/* Add relative positioning to the parent container */
div[v-else] {
  position: relative;
  min-height: 100vh; /* Ensures the container covers the entire viewport */
}

.ExitButton {
  position: absolute; /* Absolute position inside the parent */
  bottom: 10px; /* Position it near the bottom */
  left: 50%; /* Horizontally center */
  transform: translateX(-50%); /* Fine-tunes the centering */
}

.segmented-video {
  position: absolute;
  top: 50%;
  left: 35%;
  transform: translate(-50%, -50%);
  width: 70%; /* Adjust width as needed */
  max-width: 800px; /* Maximum width */
}

/* Masked Video (Smaller and in Upper-Right Corner) */
.masked-video {
  position: absolute;
  top: 65px; /* Adjust distance from the top */
  right: 280px; /* Adjust distance from the right */
  width: 300px; /* Reduce width */
  max-width: 300px; /* Define a reasonable max width */
  height: auto; /* Maintain aspect ratio */
} 

.area-display {
  position: absolute;
  bottom: 100px;
  right: 150px;
}

</style>
