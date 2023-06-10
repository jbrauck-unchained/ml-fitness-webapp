import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:5000', // Replace with your Flask backend URL
});

export const sendAPIRequest = (data) => {
  return API.post('/api/endpoint', data);
};
