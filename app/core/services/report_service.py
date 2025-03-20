# app/core/services/report_service.py
from app.core.tables.test_runs import TestRunRepository
from app.core.tables.test_cases import TestCaseRepository
from app.core.tables.test_results import TestResultRepository
import uuid


class ReportService:
    def __init__(self):
        # Any necessary initialization (e.g., logging)
        pass

    @staticmethod
    def upload_test_results(results):
        """
        Insert parsed test results into the database.

        :param results: List of parsed test results containing 'caseId' and 'payload'.
        Each 'payload' contains test status, elapsed time, and any comments.
        """
        run_id = str(uuid.uuid4())  # Generate a new UUID for the test run

        # Create test run record once for all the results
        TestRunRepository.insert_test_run(run_id, 'Automated Test Run', 'Postgres', 'Linux', '2025-03-19', 'v1.0')

        for result in results:
            payload = result['payload']
            test_ids = payload['test_ids'].split(',')
            case_id = TestCaseRepository.test_case_exists(test_ids[0])
            print(case_id)

            # Check if the test case already exists 
            if case_id is None:
                # Insert the test case if it doesn't exist
                TestCaseRepository.insert_test_case(
                    payload['name'],
                    'QA',  # Assuming static value for 'team', can be adjusted if needed
                    'http://example.com',  # Assuming static URL, can be adjusted if needed
                    payload['test_ids'],
                    payload['app_name']
                )

            elif not TestCaseRepository.test_case_exists(payload['test_ids']):
                # Update the test case if it already exists
                TestCaseRepository.update_test_case(
                    case_id,
                    payload['name'],
                    'QA',  # Assuming static value for 'team', can be adjusted if needed
                    'http://example.com',  # Assuming static URL, can be adjusted if needed
                    payload['test_ids'],
                )

            # Insert the test result record
            # self.insert_test_result(run_id, case_id, payload)

    @staticmethod
    def insert_test_result(run_id, case_id, payload):
        """
        Insert a new test result into the database.

        :param run_id: The unique test run ID.
        :param case_id: The unique test case ID.
        :param payload: The payload containing the test result details.
        """
        TestResultRepository.insert_failed_test(
            run_id,
            case_id,
            payload['status_id'],
            payload['elapsed'],
            payload['comment'],
            ''  # Placeholder for logs, can be adjusted if necessary
        )
