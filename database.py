import psycopg2
import os

# URL to the PostgreSQL database in Docker
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the PostgreSQL database
def get_conn():
    url = os.getenv("DATABASE_URL")
    if not url:
        raise ValueError("DATABASE_URL is not set")
    return psycopg2.connect(url)

# Save results from website query into database
def save_result(result):

    # Establish a connection to the database
    conn = get_conn()

    # Create a cursor to query database
    cur = conn.cursor()

    # Insert values into database
    cur.execute("""
        INSERT INTO checks (url, status, status_code, latency, error)
        VALUES (%s, %s, %s, %s, %s)
    """, (

        # URL of the website that was checked
        result["url"],

        # Status of the check (up or down)
        result["status"],

        # HTTP status code (200, 404, etc.)
        result.get("status_code"),

        # Time to get a response
        result.get("latency"),

        # Error if it failed; else null
        result.get("error")
    ))

    # Save changes
    conn.commit()

    # Close cursor
    cur.close()

    # End connection
    conn.close()