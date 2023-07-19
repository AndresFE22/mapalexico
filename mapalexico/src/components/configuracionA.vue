<template>
  <v-container>
    <!-- Selector de vistas -->
    <v-row class="view-selector">
      <div>
        <v-btn @click="mostrarVista('agregar')" :color="vistaActual === 'agregar' ? 'primary' : ''">
          Agregar Palabras
        </v-btn>
      </div>
      <div>
        <v-btn @click="mostrarVista('administrar')" :color="vistaActual === 'administrar' ? 'primary' : ''">
          Administrar Palabras
        </v-btn>
      </div>
    </v-row>
    <br>
    <v-card>
      <!-- Vista de Agregar Palabras -->
      <v-card v-if="vistaActual === 'agregar'">
        <v-card-title>AGREGAR TÉRMINOS</v-card-title>
        <v-card-text>
          <span style="font-weight: bold; font-size: large;">Agregue los términos a sus comunas correspondiente, puede agregar un término a varias comuna</span>
          <v-text-field v-model="nuevoTermino" label="Término"></v-text-field>
          <v-select
            v-model="comunasSeleccionadas"
            :items="comunas"
            multiple
            label="Selecciona Comunas"
          ></v-select>
          <v-btn @click="agregarPalabra">Agregar</v-btn>
        </v-card-text>
      </v-card>

      <!-- Vista de Administrar Palabras -->
     <!-- Vista de Administrar Palabras -->
<v-card v-if="vistaActual === 'administrar'">
  <v-card-title>Administrar Palabras</v-card-title>
  <v-card-text>
    <v-list>
      <v-list-item-group v-if="Object.keys(palabrasDict).length > 0">
        <v-list-item v-for="(comunas, palabra) in palabrasDict" :key="palabra">
          <v-list-item-content>
            <v-list-item-title>
              {{ palabra }} - <v-btn text @click="editarPalabra(palabra)">Editar</v-btn>
            </v-list-item-title>
          </v-list-item-content>
          <v-list-item-action v-if="palabra === palabraEditada">
            <v-select
              v-model="comunasSeleccionadas"
              :items="comunasDisponibles.concat(comunas)"
              multiple
              label="Selecciona Comunas"
            ></v-select>
          </v-list-item-action>
        </v-list-item>
      </v-list-item-group>
      <v-list-item v-else>
        <v-list-item-content>No hay palabras agregadas</v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card-text>
  <v-card-actions v-if="Object.keys(palabrasDict).length > 0">
    <v-btn text @click="guardarCambios">Guardar cambios</v-btn>
  </v-card-actions>
</v-card>


      <!-- Botón para volver a Inicio -->
      <v-btn @click="volverAInicio" class="home-button">Volver a Inicio</v-btn>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      nuevoTermino: '',
      comunasSeleccionadas: [],
      palabraEditada: '',
      comunas: ['Comuna 1', 'Comuna 2', 'Comuna 3', 'Comuna 4', 'Comuna 5', 'Comuna 6', 'Comuna 7', 'Comuna 8', 'Comuna 9'],
      comunasDisponibles: [],
      palabras: [],
      vistaActual: 'agregar'
    };
  },
  methods: {
    volverAInicio() {
      // Implementa la lógica para volver a la página de inicio
    },
    mostrarVista(vista) {
      this.vistaActual = vista;
    },

    agregarPalabra() {
      const nuevoTermino = {
        nuevoTermino: this.nuevoTermino,
        comunasSeleccionadas: this.comunasSeleccionadas
      };

      axios.post('http://localhost:5000/api/palabras', nuevoTermino)
        .then(response => {
          console.log('Palabra agregada correctamente:', response.data);
        })
        .catch(error => {
          console.error('Error al agregar palabra:', error);
        });

      // Reiniciar campos de entrada
      this.nuevoTermino = '';
      this.comunasSeleccionadas = [];
    },

    editarPalabra(palabra) {
      this.palabraEditada = palabra;
      this.comunasSeleccionadas = this.palabrasDict[palabra];
    },

    obtenerPalabras() {
      axios.get('http://localhost:5000/api/terminos')
        .then(response => {
          this.palabras = [];

          for (const [palabra, comunas] of Object.entries(response.data)) {
            this.palabras.push({
              palabra: palabra,
              comunas: comunas
            });
          }

          if (this.palabras.length === 0) {
            console.warn('No hay palabras agregadas');
          }

          this.palabrasDict = {};
          this.palabras.forEach(palabra => {
            this.palabrasDict[palabra.palabra] = palabra.comunas;
          });

          // Obtener todas las comunas disponibles
          const comunasUnicas = new Set();
          this.palabras.forEach(palabra => {
            palabra.comunas.forEach(comuna => {
              comunasUnicas.add(comuna);
            });
          });
          this.comunasDisponibles = this.comunas.filter(comuna => !comunasUnicas.has(comuna));
        })
        .catch(error => {
          console.error('Error al obtener palabras:', error);
        });
    },

    guardarCambios() {
      // Iteramos sobre las palabras y guardamos los cambios en cada una de ellas
      for (const palabra in this.palabrasDict) {
        axios.post(`http://localhost:5000/api/palabras/${palabra}`, {
          comunasSeleccionadas: this.palabrasDict[palabra]
        })
        .then(response => {
          console.log(`Cambios guardados correctamente para ${palabra}:`, response.data);
        })
        .catch(error => {
          console.error(`Error al guardar cambios para ${palabra}:`, error);
        });
      }
      this.palabraEditada = ''; 
    }
  },

  created() {
    this.obtenerPalabras();
  }
};
</script>

<style>
.view-selector {
  justify-content: center;
  margin-top: 20px;
}

.home-button {
  position: absolute;
  bottom: 20px;
  right: 20px;
}
</style>
