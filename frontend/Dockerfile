# Base image
FROM node:lts-alpine

# Install serve package globally
RUN npm i -g serve

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json from the intelli-app folder
COPY intelli-app/package*.json ./

# Install project dependencies
RUN npm install

# Copy the project files from the intelli-app folder
COPY intelli-app/. .

# Build the project
RUN npm run build

# Expose a port
EXPOSE 5000

# Executable
CMD ["serve", "-s", "dist", "-l", "80"]
