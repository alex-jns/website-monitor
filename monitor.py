import requests
import time

# Imports the function from database.py
from database import save_result

# Imports the function from alerts.py
from alerts import send_alert

# Array of websites to iterate over
URLS = [
    "https://google.com",
    "https://x.com"
]

# Monitors the websites and returns information
def check_site(url):
    
    # Start the clock
    start = time.time()

    try:
        
        # Send an HTTP request to the website; waits 5 seconds before failing
        response = requests.get(url, timeout=5)

        # Subtract time from start time to get latency; time to get response
        latency = time.time() - start

        # Status code 200 represents a successful connection
        status = "up" if response.status_code == 200 else "down"

        # Python dictionary
        return {
            "url": url,
            "status": status,
            "status_code": response.status_code,
            "latency": latency
        }
    
    # General error catch; e is the error message
    except Exception as e:
        return {
            "url": url,
            "status": "down",
            "error": str(e),
            "latency": None
        }

# Main monitoring loop
def run():

    # Iterate over the array
    for url in URLS:

        # Result of check_site function (Python dictionary)
        result = check_site(url)

        # Save results to the database
        save_result(result)

        # Send alert is necessary
        if result["status"] == "down":
            send_alert(result)

# Python entry point check
if __name__ == "__main__":
    run()