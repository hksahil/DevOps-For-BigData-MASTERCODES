# Dockerfile

# Use the official Python image from Docker Hub
FROM python:latest

# Metadata
LABEL author="Sahil Choudhary"
LABEL email="officialhsahil@gmail.com"
LABEL description="This is a sample Dockerfile"

# Set the working directory inside the container
WORKDIR /home

# Copy the current directory contents into the container at /app
COPY . /home

# Install pandas, numpy, matplotlib and other dependencies if needed
RUN pip install pandas numpy matplotlib

# Expose the port the app runs on (not necessary for this script)
EXPOSE 80

# Define environment variables
ENV ENVIRONMENT=production

# Command to run when the container starts
CMD ["python", "/home/app.py"]
