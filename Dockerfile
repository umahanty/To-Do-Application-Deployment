FROM python:3.10.12-alpine AS build-stage

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Install build dependencies
RUN apk --no-cache add build-base libffi-dev openssl-dev

# Set the working directory in the container
WORKDIR /app

# Copy only requirements file to the container
COPY requirements.txt .

 Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Update PATH environment variable to include virtual environment
ENV PATH="/venv/bin:$PATH"

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]

USER umahanty
