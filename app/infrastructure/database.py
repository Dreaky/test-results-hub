import psycopg2
from psycopg2.extras import DictCursor
from app.config.settings import DB_CONFIG


def get_db_connection():
    try:
        return psycopg2.connect(**DB_CONFIG, cursor_factory=DictCursor)
    except psycopg2.OperationalError as e:
        print(f"Error connecting to database: {e}")
        raise
