<template>
  <v-container>
    <h1>{{ title }}</h1>
    <p>Here are some tasks fetched from the Flask backend:</p>

    <!-- Display List of Todos -->
    <v-list>
      <v-list-item v-for="todo in todos" :key="todo.id">
        <v-list-item-content>
          <v-list-item-title>{{ todo.title }}</v-list-item-title>
          <v-list-item-subtitle>{{ todo.description }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <!-- Error Alert -->
    <v-alert v-if="error" type="error" dismissible>
      Error: {{ error }}
    </v-alert>
  </v-container>
</template>

<script>
import api from '../services/api';  // Use the '@' alias for 'src'

export default {
  name: 'TodoList',
  data() {
    return {
      title: 'Todo List',
      todos: [],
      error: null,
    };
  },
  mounted() {
    // Fetch the todos when the component is mounted
    this.fetchTodos();
  },
  methods: {
    async fetchTodos() {
      console.log('fetchTodos called'); // Log to check when it's called
      try {
        this.error = null;  // Clear previous errors
        const response = await api.get('/todo');  // Backend route
        console.log(response.data);  // Log the response from the backend
        this.todos = response.data;  // Set the fetched todos
      } catch (err) {
        this.error = 'Failed to fetch todos. Please try again.';
        console.error('Axios error:', err);  // Log detailed error
      }
    },
  },
};
</script>
