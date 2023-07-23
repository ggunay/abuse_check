# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and configuration file into the container
COPY abuse_checker.py /app/
COPY config.env /app/

# Install necessary dependencies
RUN pip install python-whois

# Run the Python script with the desired environment variables when the container starts
CMD ["bash", "-c", "source /app/config.env && python abuse_checker.py"]
