# Website Monitoring & Alert System (WIP)

A containerized website monitoring and alerting system using Python, PostgreSQL, cron scheduling, and GitHub Actions CI/CD.

Queries a list of websites and stores them in a PostgreSQL database. Includes values such as HTTP status codes, up/down status, and latency. Runs in a Docker container, and validated through GitHub Actions CI testing.

## Todo

- Polish README and release

# Features

- Triggers via cron scheduling.
- Runs a website monitoring Python script.
- Saves information to a PostgreSQL database.
- Containerized in a Docker image.
- Validated through GitHub Actions CI testing.
- Sends E-Mail alerts if websites are down.
 
## Requirements

- Python 3.9+ or Docker
- A Gmail account with 2-Step Verification enabled
- A Google App Password (16 characters)

## Getting Started

### Clone the repository

Pull the project files from GitHub using the command:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Set up environment

This project uses a .env file to manage secrets. Create a .env file in the root directory and add the following:

```
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password-here
```

### Install dependencies

If running locally (without Docker) install the dependencies:

```
pip install -r requirements.txt
```

### Run with Docker

Navigate to the directory with the project and build the Docker image:

```
docker build -t site-monitor .
```

Finally, run the container:

```
docker run --env-file .env site-monitor
```

## Usage

To be determined
