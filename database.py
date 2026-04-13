import psycopg2
import os

# URL to the PostgreSQL database in Docker
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the PostgreSQL database
def get_conn():
    return psycopg2.connect(DATABASE_URL)

# Save results from website query into database
def save_result(result):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO checks (url, status, status_code, latency, error)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        result["url"],
        result["status"],
        result.get("status_code"),
        result.get("latency"),
        result.get("error")
    ))

    conn.commit()
    cur.close()
    conn.close()