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

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Copy crontab
COPY crontab /etc/cron.d/monitor
RUN chmod 0644 /etc/cron.d/monitor && crontab /etc/cron.d/monitor

RUN touch /var/log/cron.log

# Entrypoint dumps Docker env vars so cron can see them
CMD env >> /etc/environment && cron -f