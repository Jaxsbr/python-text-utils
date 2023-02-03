# Use an existing image as the base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the python script to the working directory
COPY text_mop.py .

# Define a build-time argument
ARG FILE_NAME

# Run the script when the container starts and pass the text file name as an argument
CMD ["python", "text_mop.py", "${FILE_NAME}"]
