-- Creates a table if one does not already exist
CREATE TABLE IF NOT EXISTS checks (

    -- Unique identifier
    id SERIAL PRIMARY KEY,

    -- URL of the website that was checked
    url TEXT,

    -- Status of the request (up or down)
    status TEXT,

    -- HTTP code returned by the website (200, 404, etc.)
    status_code INT,

    -- How long it took to get a response
    latency FLOAT,

    -- Error message if request failed; else null
    error TEXT,

    -- Timestamp when check was performed; time taken when record is inserted
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);