import uuid
from app.infrastructure.database import execute_query

status_map = {
    1: 'passed',
    2: 'blocked',
    3: 'untested',
    4: 'retest',
    5: 'failed',
    6: 'skipped',
    7: 'failed_repeated',
    8: 'flaky',
}


class TestResultTable:
    @staticmethod
    def insert_failed_test(tc_id, run_id, status, elapsed, error_message, log_url):
        result_id = str(uuid.uuid4())
        if isinstance(tc_id, list):
            tc_id = tc_id[0]
        query = """
            INSERT INTO test_results (id, tc_id, run_id, status, elapsed, error_message, log_url) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (tc_id, run_id) DO NOTHING 
        """
        execute_query(query, (result_id, tc_id, run_id, status_map[status], elapsed, error_message, log_url))
        return result_id
