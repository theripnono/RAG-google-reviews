// src/services/api.js
import axios from 'axios';

// Create an Axios instance
const api = axios.create({
    baseURL: 'http://127.0.0.1:5000/api/todo', // Flask backend URL with API prefix
    timeout: 10000, // Optional timeout for requests
    headers: {
        'Content-Type': 'application/json',
    },
});

export default api;
