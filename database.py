import sqlite3

DB_NAME = "users.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT,
        language TEXT DEFAULT 'ar',
        bombs INTEGER DEFAULT 3,
        predictions INTEGER DEFAULT 0,
        is_banned INTEGER DEFAULT 0,
        joined_at TEXT,
        last_seen TEXT
    )
    """)

    conn.commit()
    conn.close()
