<template>
  <v-container>
    <v-card class="chat-card">
      <v-card-title class="text-center">Get insights from the reviews</v-card-title>
      <v-card-text class="chat-container">
        <v-list>
          <v-list-item v-for="message in messages" :key="message.id">
            <v-list-item-content :class="message.author">
              <v-row>
                <v-col>
                  <!-- Show loading state or message content -->
                  <div v-if="message.loading" class="loading-message">
                    <v-progress-circular
                      indeterminate
                      size="20"
                      width="2"
                      color="primary"
                      class="mr-2"
                    ></v-progress-circular>
                    Processing your request...
                  </div>
                  <div v-else>{{ message.content }}</div>
                </v-col>
              </v-row>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-text-field
          v-model="newMessage"
          label="Write your message"
          @keyup.enter="sendMessage"
          class="message-input"
          outlined
          :disabled="isLoading"
        ></v-text-field>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import api from '../services/api';

export default {
  data() {
    return {
      messages: [],
      newMessage: '',
      isLoading: false,
    };
  },
  methods: {
    async sendMessage() {
      if (!this.newMessage.trim() || this.isLoading) return;
      
      const userMessage = this.newMessage;
      // Add user message to the list
      this.messages.push({ content: userMessage, author: 'user' });
      
      // Add a loading message placeholder
      this.messages.push({ 
        loading: true, 
        content: '', 
        author: 'bot' 
      });
      
      // Clear input and set loading state
      this.newMessage = '';
      this.isLoading = true;

      try {
        // Make the POST request to your API
        const response = await api.post('/reviews-insights', { 
          question: userMessage 
        });
        
        // Replace loading message with actual response
        this.messages.pop(); // Remove loading message
        this.messages.push({ 
          content: response.data.data, 
          author: 'bot',
          loading: false
        });
      } catch (error) {
        // Replace loading message with error
        this.messages.pop(); // Remove loading message
        this.messages.push({ 
          content: 'Lo siento, hubo un error al obtener la información.', 
          author: 'bot',
          loading: false
        });
        console.error(error);
      } finally {
        this.isLoading = false;
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

.loading-message {
  display: flex;
  align-items: center;
  color: #666;
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