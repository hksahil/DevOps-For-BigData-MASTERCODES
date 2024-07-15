# This is my first Dockerfile
# COMMANDS expression
## FROM
## ADD
## COPY
## ENV
## WORKDIR
## CMD 

# FROM Command - Import a base Image
FROM python:latest

# RUN Command - Used to install dependencies 
# Shell Syntax
# RUN pip install pandas

# Exec Syntax
RUN ["pip","install","pandas"]

# WORKDIR - It is used to set the working folder in container
WORKDIR /desktop/newfolder

# USER - Setup users for your containers
RUN  useradd -ms /bin/bash sahiluser
USER sahiluser

# ENV - Set environment variables
ENV app_host='0.0.0.0'
ENV app_port=5000

# COPY - Copy files from your local computer to container
COPY app.py /desktop/newfolder

# ADD - Copy files from cloud to container
ADD https://ziiorjpxvfhhwhcrpkfk.supabase.co/storage/v1/object/public/Static_resources/Screenshot_2024-06-28_at_11.08.01_PM.png?t=2024-06-29T21%3A09%3A40.755Z  /desktop/newfolder

# EXPOSE - Opens a port on your computer
EXPOSE 5000

CMD ls /desktop/newfolder

