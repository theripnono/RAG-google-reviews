# Base image
FROM node:lts-alpine

# Install serve package
RUN npm i -g serve

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./ 

# Install project dependencies
RUN npm install

# Copy the project files
COPY . .

# Build the project
RUN npm run build

# Expose a port
EXPOSE 5000

# Executables
# Use the -l option to specify port 80 for serve. Update CMD
CMD [ "serve", "-s", "dist", "-l", "80" ]
