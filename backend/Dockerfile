# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /weather

# Copy the current directory contents into the container at /weather
COPY . /weather/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD gunicorn config.wsgi:application -b 0.0.0.0:8000
