#FROM ubuntu:latest
#LABEL authors="Chad"
#
#ENTRYPOINT ["top", "-b"]
# Use a lightweight Python base image
#FROM python:3.9-slim

# Change from python:3.9-slim to python:3.9-alpine
FROM python:3.9-alpine

# Alpine requires some extra build steps for certain packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run the application

CMD ["python", "app.py"]
