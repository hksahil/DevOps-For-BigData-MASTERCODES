# Dockerfile

# Use the official Python image from Docker Hub
FROM python:latest

# Metadata
LABEL author="Your Name"
LABEL email="your.email@example.com"
LABEL description="Dockerfile for Python application with multiple modules"

# Set the working directory inside the container
WORKDIR /app

# Copy all contents of the current directory into the container at /app
COPY . .

# Command to run when the container starts
CMD ["python", "app.py"]
