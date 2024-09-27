# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose the port the app will run on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
