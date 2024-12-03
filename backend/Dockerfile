# Use a Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the backend dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY * ./

# Expose the backend port
EXPOSE 5500

# Start the backend
CMD ["python", "app.py"]
