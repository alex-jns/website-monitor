CREATE TABLE IF NOT EXISTS checks (
    id SERIAL PRIMARY KEY,
    url TEXT,
    status TEXT,
    status_code INT,
    latency FLOAT,
    error TEXT,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);