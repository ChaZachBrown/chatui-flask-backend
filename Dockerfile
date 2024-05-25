# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5001

# Define environment variables
ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
