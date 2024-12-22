import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/',
});


export default {
  // POST request to analyze the URL
  post(endpoint, payload) {
    return api.post(endpoint, payload);
  },

  get(endpoint, params = {}) {
    return api.get(endpoint, { params });  // For GET requests, passing query params
  },

};