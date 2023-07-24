<template>
    <div class="container">
      <h1 >Inicio de sesión</h1>
      <v-form @submit="login">
        <v-text-field v-model="username" label="Nombre de usuario"></v-text-field>
        <v-text-field v-model="password" label="Contraseña" type="password"></v-text-field>
        <v-btn dark type="submit">Iniciar sesión</v-btn>
      </v-form>
      <br>
      <div v-if="showError" class="error-message">
        Usuario o contraseña incorrectos
      </div>
    </div>
  </template>
  
  <script>
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        showError: false,
      };
    },
    name: 'loginL',
    methods: {
      login() {
        // Aquí puedes realizar la validación del inicio de sesión con las credenciales proporcionadas
        // Por simplicidad, utilizaremos credenciales predefinidas para el ejemplo
        if (this.username === 'usuario' && this.password === 'contraseña') {
          // Redirigir al usuario a la página de inicio después del inicio de sesión exitoso
          this.$router.push('/inicio');
        } else {
          this.showError = true;
          setTimeout(() => {
            this.showError = false;
          }, 2000);
        }
      },
    },
  };
  </script>
  
  <style>
  .container {
    margin-top: 4%;
    overflow: hidden;
    background-color: white;
  }
  
  .error-message {
    background-color: #f44336;
    color: white;
    padding: 10px;
    border-radius: 4px;
    text-align: center;
  }
  
  @media (max-width: 600px) {
    .container {
      margin-top: 12%;
    }
  }
  </style>
  