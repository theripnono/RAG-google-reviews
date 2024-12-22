import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/',
});


export default {
  // POST request to analyze the URL
  post(endpoint, payload) {
    return api.post(endpoint, payload);
  },

  chatpage(payload) {
    return api.post('chat', payload);  // 'new-page-url' is your new endpoint
  },

};