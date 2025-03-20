from app.infrastructure.database import execute_query


class TestRunRepository:
    @staticmethod
    def insert_test_run(run_id, name, database, os, date, version):
        query = """
            INSERT INTO test_run (id, name, database, os, ci, date, version, total_tests, failed_tests) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, 0, 0)
            ON CONFLICT (id) DO NOTHING;
        """
        execute_query(query, (run_id, name, database, os, "CI_TOOL", date, version))
