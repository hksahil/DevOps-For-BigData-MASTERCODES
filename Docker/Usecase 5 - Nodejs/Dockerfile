# Dockerfile

# Use the official Node.js image from Docker Hub
FROM node:latest

# Metadata
LABEL author="Your Name"
LABEL email="your.email@example.com"
LABEL description="Dockerfile for Node.js application"

# Set working directory inside the container
WORKDIR /app

# Copy all local files into the image
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["node", "app.js"]
