import { createRouter, createWebHistory } from 'vue-router';
import Landing from '../components/Landing.vue';
import ChatLLM from '../components/ChatLLM.vue';

const routes = [
    {
        path: '/',
        name: 'Landing',
        component: Landing,
    },
    {
        path: '/chat',
        name: 'ChatLLM',
        component: ChatLLM,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});


export default router;
