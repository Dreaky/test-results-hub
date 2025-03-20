from app.infrastructure.database import get_db_connection

class TestResultRepository:
    @staticmethod
    def insert_failed_test(result_id, tc_id, run_id, status, elapsed_time, tag, notes, report_url):
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO test_result (id, tc_id, run_id, status, elapsed, tag, notes, html_report) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
            ON CONFLICT (id) DO NOTHING;
        """
        cur.execute(query, (result_id, tc_id, run_id, status, elapsed_time, tag, notes, report_url))
        conn.commit()
        cur.close()
        conn.close()



        