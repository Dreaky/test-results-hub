from app.infrastructure.database import get_db_connection

class TestRunRepository:
    @staticmethod
    def insert_test_run(run_id, name, database, os, date, version):
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO test_run (id, name, database, os, date, version) 
            VALUES (%s, %s, %s, %s, %s, %s) 
            ON CONFLICT (id) DO NOTHING;
        """
        cur.execute(query, (run_id, name, database, os, date, version))
        conn.commit()
        cur.close()
        conn.close()