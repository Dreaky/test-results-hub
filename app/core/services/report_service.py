# app/core/services/report_service.py
import os
from dotenv import load_dotenv
from app.core.tables.test_runs import TestRunTable
from app.core.tables.test_cases import TestCaseTable
from app.core.tables.test_results import TestResultTable

# Load environment variables from .env file
load_dotenv()


class ReportService:
    def __init__(self):
        # Any necessary initialization (e.g., logging)
        pass

    @staticmethod
    def create_test_run(total, report_url):
        run_name = os.getenv('TEST_RUN_NAME')
        database = os.getenv('TEST_RUN_DATABASE')
        deployment = os.getenv('TEST_RUN_DEPLOY')
        run_date = os.getenv('TEST_RUN_DATE')
        version = os.getenv('TEST_RUN_VERSION')

        # Create test run record once for all the results
        run_id = TestRunTable.insert_test_run(run_name, database, deployment, run_date, version, total, report_url)

        return run_id

    @staticmethod
    def upload_test_results(run_id, results):
        for result in results:
            payload = result['payload']
            test_ids = payload['test_ids'].split(',')
            tc_id = TestCaseTable.test_case_exists(test_ids[0])
            print(tc_id)

            # Check if the test case already exists 
            if tc_id is None:
                # Insert the test case if it doesn't exist
                tc_id = TestCaseTable.insert_test_case(
                    payload['name'],
                    'QA',  # Assuming static value for 'team', can be adjusted if needed
                    'http://example.com',  # Assuming static URL, can be adjusted if needed
                    payload['test_ids'],
                    payload['app_name']
                )

            elif not TestCaseTable.test_case_exists(payload['test_ids']):
                # Update the test case if it already exists
                TestCaseTable.update_test_case(
                    tc_id,
                    payload['name'],
                    'QA',  # Assuming static value for 'team', can be adjusted if needed
                    'http://example.com',  # Assuming static URL, can be adjusted if needed
                    payload['test_ids'],
                )

            if payload['status_id'] in [5]:
                print('anp test je failed')
                TestResultTable.insert_failed_test(
                    tc_id,
                    run_id,
                    payload['status_id'],
                    payload['elapsed'],
                    payload['comment'],
                    'log_url'
                )
