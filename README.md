# IntelliReview App
It retrieves and stores reviews from Google Reviews, processing them for efficient querying. By employing Retrieval-Augmented Generation (RAG) techniques, the app enhances search capabilities, allowing users to query the downloaded reviews interactively and contextually. 

The application integrates Flask as a REST API backend and Vue.js for the frontend.


Paste the establishment url, it must be similar to:

**e.g:**

        https://www.google.com/maps/place/Restaurante+Estebenea/@43.3230991,-1.7906561,17z/data=!3m1!4b1!4m6!3m5!1s0xd51094970158069:0x5c583bb237c9fef2!8m2!3d43.3230991!4d-1.7906561!16s%2Fg%2F11svcc805z?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D

## Steps
Build the docker image 🐋 with the following command:

    docker-compose build 
    docker-compose up -d 

    Localhost:
    http://localhost:8080/
    
Create an .ENV file in the backend folder with your personal API-KEY.

        OPENAI_API_KEY='your-api-key'
        
## Preview
![preview_app](https://github.com/user-attachments/assets/f85ed9c7-3cf1-4b65-b884-a35d84ed03ac)
