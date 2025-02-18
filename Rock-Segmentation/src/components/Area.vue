<script lang="ts">
export default {
  data() {
    return {
      area: 0,
      areaURL: 'http://127.0.0.1:5000/video/area',
      eventSource: null as EventSource | null, // Armazena a referência do EventSource
    };
  },
  mounted() {
    this.updateArea(); // Chama a função ao montar o componente
  },
  methods: {
    updateArea() {
      this.eventSource = new EventSource(this.areaURL);
      console.log('Chamou Update Area')

      // Evento quando uma nova área for recebida
      this.eventSource.onmessage = (event) => {
        console.log('Recebeu atualização')
        this.area = parseFloat(event.data); // Garante que a área seja um número
        console.log(`Área recebida: ${this.area}`);
      };

      // Caso ocorra algum erro na conexão
      this.eventSource.onerror = (error) => {
        console.error('Erro ao receber os dados da área:', error);
        if (this.eventSource) {
          this.eventSource.close(); // Fecha a conexão em caso de erro
          this.eventSource = null;
        }
      };
    }
  },
  beforeUnmount() {
    // Fecha a conexão SSE ao desmontar o componente
    if (this.eventSource) {
      this.eventSource.close();
      this.eventSource = null;
    }
  }
};
</script>

<template>
  <div class="area-display">
    Área:{{ area }} px
  </div>
</template>

<style scoped>
.area-display{
  width: 8.5rem;
  height: 1.5rem;
  padding: 0.5rem 1rem;
  border-radius: 2rem;
  font-weight: 700;
  color: var(--creme, #040404);
  background: var(--coral, #f9f9f9);
  box-shadow: 4px 4px 15px 0px rgba(6, 6, 6, 0.25);
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
