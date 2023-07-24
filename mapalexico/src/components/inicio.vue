<template>
  <v-container class="fondo">
    <v-row class="row">
      <!-- Botones de comuna (solo en dispositivos móviles) -->
      <v-col v-if="$vuetify.breakpoint.xsOnly" cols="12">
        <v-row>
          <v-col v-for="comuna in comunas" :key="comuna" cols="6">
            <v-btn @click="mostrarMapa(comuna)" block
            :color="comunaSeleccionada === comuna ? 'primary' : 'white'">{{ comuna }}</v-btn>
          </v-col>
        </v-row>
      </v-col>

      <v-row>
        <v-col v-if="!$vuetify.breakpoint.xsOnly" cols="3">
        <div class="btn-container">
          <v-btn
              class="btn"
              v-for="comuna in comunas"
              :key="comuna"
              @click="mostrarMapa(comuna)"
              :color="comunaSeleccionada === comuna ? 'primary' : 'white'"
            >
              {{ comuna }}
            </v-btn>
        </div>
      </v-col>

      <v-col :cols="$vuetify.breakpoint.xsOnly ? 12 : 6">
        <iframe ref="mapa" :src="mapaUrl" width="100%" height="680"></iframe>
      </v-col>
    </v-row>

      <!-- Caja de búsqueda de palabras (solo en dispositivos móviles) -->
      <v-col v-if="$vuetify.breakpoint.xsOnly" cols="12">
        <div class="search-container">
          <v-text-field v-model="busqueda" type="text" placeholder="Buscar palabra" @input="realizarBusqueda"></v-text-field> 
        </div>
      </v-col>

      <!-- Lista de palabras (solo en dispositivos móviles) -->
      <v-col v-if="$vuetify.breakpoint.xsOnly" cols="12">
        <div class="word-container">
          <ul class="word-list">
            <li v-for="palabra in palabras" :key="palabra.palabra" class="word-item">
              <div class="word-box">
                <p class="word-text">{{ palabra }}</p>
              </div>
            </li>
          </ul>
        </div>
      </v-col>

      <!-- Caja de búsqueda y lista de palabras (solo en pantallas grandes) -->
      <v-col v-if="!$vuetify.breakpoint.xsOnly" cols="2">
        <div class="search-container">
          <v-text-field v-model="busqueda" type="text" placeholder="Buscar palabra" @input="realizarBusqueda"></v-text-field> 
        </div>
        <div class="word-container">
          <ul class="word-list">
            <li v-for="palabra in palabras" :key="palabra.palabra" class="word-item">
              <div class="word-box">
                <p class="word-text">{{ palabra }}</p>
              </div>
            </li>
          </ul>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import axios from 'axios';

export default {
  name: 'inicioC',
  data() {
    return {
      mapaUrls: {
        monteria: 'https://www.google.com/maps/d/embed?mid=1Z3zNCXWCoFiz-3CXLTI--4yoougXbSqd&ehbc=2E312F',
        'Comuna 1': 'https://www.google.com/maps/d/embed?mid=1sGtUBNn1t56F-_vN1VeBfTLqD4chOREw&ehbc=2E312F',
        'Comuna 2': 'https://www.google.com/maps/d/embed?mid=1yhzIKq2qRtst39cyyjdRf-3K5RulXZr2&ehbc=2E312F',
        'Comuna 3': 'https://www.google.com/maps/d/embed?mid=1kfVWDlnRBb7tg8CBa12o3KPOPUaKt4sG&ehbc=2E312F',
        'Comuna 4': 'https://www.google.com/maps/d/embed?mid=12-F1xq5M3_vEd1GBFWdiwteEZtiQORlK&ehbc=2E312F',
        'Comuna 5': 'https://www.google.com/maps/d/embed?mid=13K7BndeZl5plt5Yr_CZ5KZOznVSldQf9&ehbc=2E312F',
        'Comuna 6': 'https://www.google.com/maps/d/embed?mid=1Dfkk95_HPtpsBDOwna606s3clZ_Jnfax&ehbc=2E312F',
        'Comuna 7': 'https://www.google.com/maps/d/embed?mid=1pb6yRMcQ0zbuf_vIqdFejKs4vZ-npMJK&ehbc=2E312F',
        'Comuna 8': 'https://www.google.com/maps/d/embed?mid=1wBKoV-ra23aHoaZ_7u64Md49XNAhcNMg&ehbc=2E312F',
        'Comuna 9': 'https://www.google.com/maps/d/embed?mid=1S9Rvg4EQQ011fMVDf7Pv7B5j3nMkKgPq&ehbc=2E312F',
      },
      comunas: ['monteria', 'Comuna 1', 'Comuna 2', 'Comuna 3', 'Comuna 4', 'Comuna 5', 'Comuna 6', 'Comuna 7', 'Comuna 8', 'Comuna 9'],
      comunaSeleccionada: null,
      palabras: [],
      palabrasOriginal: [],
      busqueda: '',
    };
  },

  mounted() {
    this.mostrarMapa('monteria');
  },
  methods: {
    mostrarMapa(comuna) {
      this.mapaUrl = this.mapaUrls[comuna];
      this.comunaSeleccionada = comuna;
      this.obtenerPalabrasPorComuna(comuna);
    },
    obtenerPalabrasPorComuna(comuna) {
      axios
        .get(`http://localhost:5000/api/comunas/${comuna}/palabras`)
        .then(response => {
          console.log(response.data);
          this.palabras = response.data;
          this.palabrasOriginal = [...response.data];
        })
        .catch(error => {
          console.error(error);
        });
    },
    realizarBusqueda() {
      if (this.busqueda) {
        this.palabras = this.palabrasOriginal.filter(palabra => palabra.toLowerCase().includes(this.busqueda.toLowerCase()));
      } else {
        this.palabras = [...this.palabrasOriginal];
      }
    },
  },
};
</script>

<style>
@media (min-width: 600px) {
  .btn-container {
    display: flex;
    flex-direction: column;
  }
 
}

.active-btn {
  background-color: #1976d2; /* Cambiar al color deseado */
  color: white;
}

.fondo {
background-color: white;
padding: 2%;
border-radius: 20px;
}

.btn-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

.btn {
  margin-bottom: 15%;
}


.word-text {
  font-weight: bold;
  font-size: large;
  padding: 2%;
  color: white;
}

.word-box {
  background-color: rgb(67, 164, 255);
  border-radius: 20px;
}

</style>
