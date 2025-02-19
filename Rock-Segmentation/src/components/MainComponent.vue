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
      this.atFirstPage = !this.atFirstPage; 
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
  font-size: 3rem; 
  color: #FFFAF3; 
  text-align: center; 
  font-weight: bold; 
  position: absolute; 
  top: 0px; 
  left: 50%; 
  transform: translateX(-50%); 
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); 
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


div[v-else] {
  position: relative;
  min-height: 100vh; 
}

.ExitButton {
  position: absolute; 
  bottom: 10px; 
  left: 50%; 
  transform: translateX(-50%); 
}

.segmented-video {
  position: absolute;
  top: 50%;
  left: 35%;
  transform: translate(-50%, -50%);
  width: 70%; 
  max-width: 800px; 
}

.masked-video {
  position: absolute;
  top: 65px; 
  right: 280px; 
  width: 300px; 
  max-width: 300px; 
  height: auto; 
} 

.area-display {
  position: absolute;
  bottom: 100px;
  right: 150px;
}

</style>
