<template>
  <v-app>
    <v-main class="main-content">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
/* Global styles */
.v-application {
  background-image: url('./assets/img/map.png') !important;
  background-size: cover !important;
}

.main-content {
  min-height: 100vh;
}
</style>