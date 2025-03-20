import uuid
from app.infrastructure.database import execute_query


class TestRunTable:
    @staticmethod
    def insert_test_run(name, database, deployment, date, version, total, report_url=None):
        run_id = str(uuid.uuid4())  # Generate a new UUID for the test run

        # Updated query to include the new columns (total_failures, total_skipped, total_errors, total_time)
        query = """INSERT INTO test_run (id, name, database, deployment, date, version, total_tests, total_failures, 
        total_skipped, total_errors, total_time, report_url) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
        ON CONFLICT (id) DO NOTHING;"""

        # Execute the query with the new data
        execute_query(query, (
            run_id,
            name,
            database,
            deployment,
            date,
            version,
            total['total_tests'],
            total['total_failures'],
            total['total_skipped'],
            total['total_errors'],
            total['total_time'],
            report_url)
          )

        return run_id
