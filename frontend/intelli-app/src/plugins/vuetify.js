// src/plugins/vuetify.js
import 'vuetify/styles'; // Vuetify styles
import { createVuetify } from 'vuetify';
import { aliases, mdi } from 'vuetify/iconsets/mdi';

const vuetify = createVuetify({
    theme: {
        defaultTheme: 'light',
    },
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
            mdi,
        },
    },
});

export default vuetify;
