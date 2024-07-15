# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install the dependencies
RUN pip install streamlit

# Copy the rest of the application code into the container
COPY . .

# Command to run the Streamlit app

# CMD ["streamlit", "run", "app.py"]

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]