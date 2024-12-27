<template>
    <v-container>
      <v-card class="chat-card">
        <v-card-title class="text-center">Get reviews insights</v-card-title>
        <v-card-text class="chat-container">
          <v-list>
            <v-list-item v-for="message in messages" :key="message.id">
              <v-list-item-content :class="message.author">
                <v-row>
                  <v-col>{{ message.content }}</v-col>
                </v-row>
              </v-list-item-content>
            </v-list-item>
          </v-list>
          <v-text-field
            v-model="newMessage"
            label="Escribe tu mensaje"
            @keyup.enter="sendMessage"
            class="message-input"
            outlined
          ></v-text-field>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import api from '../services/api'; // Make sure to import your API service
  
  export default {
    data() {
      return {
        messages: [],
        newMessage: '',
      };
    },
methods: {
    async sendMessage() {
      const userMessage = this.newMessage;  // Store the current message before clearing it

      // Add user message to the list
      this.messages.push({ content: userMessage, author: 'user' });
      this.newMessage = '';  // Clear the input field

      try {
        // Make the POST request to your API with the user's message
        const response = await api.post('/reviews-insights', { question: userMessage });

        // Add bot's reply with the API response
        this.messages.push({ content: response.data.data, author: 'bot' });
      } catch (error) {
        // Handle error (e.g., show an error message)
        this.messages.push({ content: 'Lo siento, hubo un error al obtener la información.', author: 'bot' });
          console.error(error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .chat-card {
    max-width: 600px;
    margin: 0 auto;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  
  .chat-container {
    max-height: 400px;
    overflow-y: auto;
    padding-bottom: 20px;
    background-color: #f9f9f9;
  }
  
  .message-input {
    margin-top: 20px;
  }
  
  .user {
    background-color: #e3f2fd;
    border-radius: 8px;
    padding: 10px;
    margin: 8px 0;
    text-align: right;
  }
  
  .bot {
    background-color: #f1f8e9;
    border-radius: 8px;
    padding: 10px;
    margin: 8px 0;
    text-align: left;
  }
  
  .v-list-item-content {
    padding: 10px;
  }
  
  .v-list-item {
    margin-bottom: 10px;
  }
  
  .v-card-title {
    background-color: #1976d2;
    color: white;
    font-weight: bold;
    padding: 16px;
    border-radius: 15px 15px 0 0;
  }
  </style>
  