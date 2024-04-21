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

# Install any dependencies within a virtual environment
RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Start a new stage to create a smaller final image
FROM python:3.9-alpine AS production-stage

# Copy the virtual environment from the build stage
COPY --from=build-stage /venv /venv

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Update PATH environment variable to include virtual environment
ENV PATH="/venv/bin:$PATH"

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]

# Metadata indicating an image for production use
LABEL stage=production

# Remove all previous cache of all Docker images
RUN docker system prune -a --force

