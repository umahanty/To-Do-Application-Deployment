# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask application code into the container
COPY . /app

# Install any dependencies required by your Flask application
RUN pip install --no-cache-dir -r requirements.txt
RUN apk --no-cache add build-base libffi-dev openssl-dev
RUN pip install pytest
RUN pip install selenium

# Expose the port on which your Flask application will run
EXPOSE 5000

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Command to run the Flask application
CMD ["flask", "run"]

