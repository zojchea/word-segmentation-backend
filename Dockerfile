# Use the Python 3.11 image from DockerHub
FROM python:3.11

# Set a working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose port 80 for the application
EXPOSE 80

# Set the command to run when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
