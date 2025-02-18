<script lang="ts">
export default{
    props:{
        txt: {type: String, required: true}
    }
}
</script>

<template>
    <button class="main-button">
        {{ txt }}
    </button>
</template>

<style scoped>
.main-button {
  width: 19.5rem;
  height: 3.5rem;
  padding: 0.5rem 1rem;
  border-radius: 2rem;
  font-weight: 700;
  color: var(--creme, #040404);
  background: var(--coral, #f9f9f9);
  box-shadow: 4px 4px 15px 0px rgba(6, 6, 6, 0.25);
  cursor: pointer;
  transition: 0.2s;

  display: flex;
  justify-content: center;
  align-items: center;
}

.main-button:hover {
  background: var(--ocre-hover, #645c5c);
}
</style>