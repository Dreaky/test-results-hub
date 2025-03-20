from app.infrastructure.database import get_db_connection

class TestRunRepository:
    @staticmethod
    def insert_test_run(run_id, name, database, os, date, version):
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO test_run (id, name, database, os, ci, date, version, total_tests, failed_tests) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, 0, 0)
            ON CONFLICT (id) DO NOTHING;
        """
        cur.execute(query, (run_id, name, database, os, "CI_TOOL", date, version))
        conn.commit()
        cur.close()
        conn.close()
