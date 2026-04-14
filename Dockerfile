# Base image uses python 3.11-slim
FROM python:3.11-slim

# Working directory for the container
WORKDIR /app

# Copy this text file to /app first
COPY requirements.txt .

# Install requirements from the text file
RUN pip install -r requirements.txt

# Copy the rest of the files
COPY . .

# When the container starts, execute monitor.py using python
CMD ["python", "monitor.py"]