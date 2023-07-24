<template>
  <div id="app">
    <v-app>
      <v-app-bar app color="primary" class="bar">
        <v-toolbar-title style="font-weight: bold; color: white; padding: 2%;">Mapa sociolingüístico interactivo
<br>de la ciudad de Montería</v-toolbar-title>
<v-spacer></v-spacer>

        <v-btn icon to="/configuracion">
          <v-icon color="white">mdi-account</v-icon>
        </v-btn>
      </v-app-bar>
        <transition name="slide" mode="out-in">
          <router-view>
          </router-view>
        </transition>
    </v-app>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background-image: url(./assets/fondo.jpg);

}

.imgunicor {
  width: 2%;
}

.bar {

  height: 100px;


}
</style>
