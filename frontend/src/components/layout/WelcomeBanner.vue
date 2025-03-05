<template>
  <div class="welcome-banner-wrapper" :style="{ backgroundColor: themeColor }">
    <div class="welcome-banner">
      <h1>{{ welcomeMessage }}</h1>
      <p>{{ sectionDescription }}</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'

const store = useStore()

const themeColor = computed(() => store.state.theme.themeColor)
const welcomeMessage = computed(() => store.state.theme.welcomeMessage)
const sectionDescription = computed(() => store.state.theme.sectionDescription)
</script>

<style scoped>
.welcome-banner-wrapper {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
}

.welcome-banner {
  width: 100%;
  color: #fff;
  padding: 20px;
  text-align: center;
  box-sizing: border-box;
}

.welcome-banner h1 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.welcome-banner p {
  font-size: 1rem;
  opacity: 0.8;
}
</style> 