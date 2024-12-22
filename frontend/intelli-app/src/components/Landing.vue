<template>
  <v-container class="d-flex flex-column align-center justify-center fill-height">
    <v-card class="pa-8 text-center" style="background-color:#eeeeee">
      <v-card-title class="text-h4 font-weight-bold">
        Get insights from Google Reviews with IA
      </v-card-title>
      <v-card-text>
        <v-text-field
          v-model="url"
          label="Paste your URL here"
          outlined
          dense
          class="mt-4"
        ></v-text-field>
        <v-btn color="primary" class="mt-4" @click="analyzeUrl">Analyze</v-btn>
      </v-card-text>
    </v-card>
  </v-container>
  <v-dialog v-model="showDialog" max-width="400">
    <v-card>
      <v-card-title class="headline">Error</v-card-title>
      <v-card-text>Please provide a valid URL to analyze.</v-card-text>
      <v-card-actions>
        <v-btn color="primary" @click="showDialog = false">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import api from '../services/api';

export default {
  name: 'TodoList',
  
  data() {
    return {
      url: '',
      showDialog: false,
      isLoading: false,
    };
  },

  methods: {
    async analyzeUrl(){
      if (!this.url){
        this.showDialog = true;
        return;
      }
      
      this.isLoading = true;

      try {
        const response = await api.post('/analyze', {url: this.url});
        console.log(response.data);

      } catch (error) {
        console.error(error);
      }
    }
  },

};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}
</style>