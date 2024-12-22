<template>
  <v-layout>
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1 class="text-h4 mb-4">{{ title }}</h1>
          <p class="text-body-1 mb-6">Here are some tasks fetched from the Flask backend:</p>
        </v-col>
      </v-row>

      <!-- Loading State -->
      <v-row v-if="loading">
        <v-col cols="12">
          <v-progress-linear
            indeterminate
            color="primary"
          ></v-progress-linear>
        </v-col>
      </v-row>

      <!-- Display List of Todos -->
      <v-row>
        <v-col cols="12">
          <v-list v-if="todos.length > 0">
            <v-list-item
              v-for="todo in todos"
              :key="todo.id"
              :value="todo.id"
            >
              <template v-slot:default>
                <v-list-item-title>{{ todo.title }}</v-list-item-title>
                <v-list-item-subtitle>{{ todo.description }}</v-list-item-subtitle>
              </template>
            </v-list-item>
          </v-list>
          
          <!-- Empty State -->
          <v-card
            v-else-if="!loading && !error"
            class="pa-4 text-center"
            variant="outlined"
          >
            <v-card-text>No todos found. Create one to get started!</v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Error Alert -->
      <v-row v-if="error">
        <v-col cols="12">
          <v-alert
            type="error"
            variant="tonal"
            closable
            class="mb-4"
          >
            {{ error }}
          </v-alert>
        </v-col>
      </v-row>
    </v-container>
  </v-layout>
</template>

<script>
import api from '../services/api';

export default {
  name: 'TodoList',
  
  data() {
    return {
      title: 'Todo List',
      todos: [],
      error: null,
      loading: false,
    };
  },

  mounted() {
    this.fetchTodos();
  },

  methods: {
    async fetchTodos() {
      this.loading = true;
      this.error = null;

      try {
        const response = await api.get('/todo');
        this.todos = response.data;
      } catch (err) {
        console.error('Failed to fetch todos:', err);
        this.error = err.response?.data?.message || 
                    'Failed to fetch todos. Please try again.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.v-list {
  border-radius: 8px;
  border: 1px solid rgb(var(--v-border-color));
}

.v-list-item {
  min-height: 64px;
}

.v-list-item:not(:last-child) {
  border-bottom: 1px solid rgb(var(--v-border-color));
}
</style>