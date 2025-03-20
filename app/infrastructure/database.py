import psycopg2
from psycopg2.extras import DictCursor
from app.config.settings import DB_CONFIG


def get_db_connection():
    try:
        return psycopg2.connect(**DB_CONFIG, cursor_factory=DictCursor)
    except psycopg2.OperationalError as e:
        print(f"Error connecting to database: {e}")
        raise


def execute_query(query, params=None, fetch_result=False):
    """
    Helper function to execute a query with provided parameters.
    Returns the result if fetch_result is True.

    :param query: SQL query to be executed.
    :param params: Parameters for the SQL query.
    :param fetch_result: Whether to fetch the result of the query (default is False).
    :return: The result of the query (if fetch_result is True).
    """
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute(query, params)

    if fetch_result:
        result = cur.fetchone()  # or cur.fetchall() if expecting multiple results
    else:
        result = None

    conn.commit()
    cur.close()
    conn.close()

    return result
