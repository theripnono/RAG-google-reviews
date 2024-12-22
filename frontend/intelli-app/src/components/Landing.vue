<template>
  <div class="position-relative">
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
          <v-btn 
            color="primary"
            class="mt-4"
            :loading="isLoading"
            @click="analyzeUrl"
          >
            Analyze
          </v-btn>
        </v-card-text>
      </v-card>
    </v-container>

    <v-overlay
      :model-value="isLoading"
      class="align-center justify-center"
    >
      <div class="d-flex flex-column align-center justify-center">
        <v-progress-circular
          indeterminate
          color="primary"
          size="64"
        ></v-progress-circular>
        <h2 class="mt-4" style="color: aquamarine;">Please wait until the reviews are downloaded...</h2>
      </div>
    </v-overlay>

    <v-dialog v-model="showDialog" max-width="400">
      <v-card>
        <v-card-title class="headline">Error</v-card-title>
        <v-card-text>Please provide a valid URL to analyze.</v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="showDialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  name: 'Landing',
  
  data() {
    return {
      url: '',
      showDialog: false,
      isLoading: false,
    };
  },

  methods: {
    async analyzeUrl() {
      if (!this.url) {
        this.showDialog = true;
        return;
      }
      
      this.isLoading = true;

      try {
        const response = await api.post('/analyze', { url: this.url });
        console.log(response.data);
        this.$router.push({ name: 'ChatLLM' });
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    }
  },
};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}

.position-relative {
  position: relative;
  height: 100vh;
}
</style>