# Website Monitoring & Alert System

A containerized website monitoring and alerting system using Python, PostgreSQL, cron scheduling, and GitHub Actions CI/CD.

Queries a list of websites and stores them in a PostgreSQL database. Includes values such as HTTP status codes, up/down status, and latency. Runs in a Docker container, and validated through GitHub Actions CI testing.

# Features

- Triggers via cron scheduling.
- Runs a website monitoring Python script.
- Saves information to a PostgreSQL database.
- Containerized in a Docker image.
- Validated through GitHub Actions CI testing.
- Sends E-Mail alerts if websites are down.
 
## Requirements

- Python 3.9+
- Docker
- A Gmail account with 2-Step Verification enabled
- A Google App Password (16 characters)

## Getting Started

### Clone the repository

Pull the project files from GitHub using the command:

```
git clone https://github.com/alex-jns/website-monitor.git
cd website-monitor
```

## Set up the environment

This project uses a .env file to manage secrets. Create a .env file in the root directory.

If you do not want the default PostgreSQL login credentials, change them here:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/monitor
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=monitor
```

If you want to use the default login credentials, copy this code into your .env file.

### (Optional) Set up email alerts

This step is optional if you want to receive email alerts if a website down.

Add the following lines to your .env file:

```
EMAIL_RECIPIENT=recipient-email@gmail.com
EMAIL_SENDER=sender-email@gmail.com
EMAIL_PASS=your-app-password-here
```

### Install dependencies

If running locally (without Docker) install the dependencies:

```
pip install -r requirements.txt
```

### Run with Docker

Build and run the containers:

```
docker compose up --build
```

## Usage

Once the project is running, it will query a list of websites every 5 minutes. Websites that are down (returns a bad HTTP status code, or times out after 5 seconds) it will send an email through Gmail SMTP using TLS if the environment was set up correctly. 

### Change sites to be monitored

The sites that are monitored are located in an array named URLS in monitor.py:

```
URLS = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/10"
]
```

### Change frequency of monitoring

The monitoring script is trigger by the crontab file:

```
*/5 * * * * /usr/local/bin/python3 /app/monitor.py >> /var/log/cron.log 2>&1
```

### Query the database

Login to the database using Docker:

```
docker compose exec db psql -U postgres -d monitor
```

Input a select statement:

```
SELECT * FROM checks;
```

### Finishing up

If you want to stop the Docker containers:

```
docker compose down
```

## Troubleshooting

1. Ensure that the Raspberry Pi and sensors are properly connected and configured to send data to the backend.

> The backend is expecting a UDP message from port 11000. It is expecting a JSON response such as:

```
{
  temperatureF: 72, // expecting no quotation marks around "temperatureF"
  "temperatureC": 22,
  "humidity": 55
}
```

2. Check the console output and logs for any error messages or exceptions that may indicate issues with data collection, API integration, or report generation.
3. Verify that the OpenMeteo API is accessible and that the API parameters (latitude, longitude) are correctly configured.
4. Check for any file I/O issues when writing JSON files or generating reports, such as permission issues or insufficient disk space.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
