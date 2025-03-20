from app.infrastructure.database import execute_query


class TestResultRepository:
    @staticmethod
    def insert_failed_test(result_id, tc_id, run_id, status, elapsed_time, tag, notes, report_url):
        query = """
            INSERT INTO test_result (id, tc_id, run_id, status, elapsed, tag, notes, html_report) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
            ON CONFLICT (id) DO NOTHING;
        """
        execute_query(query, (result_id, tc_id, run_id, status, elapsed_time, tag, notes, report_url))
