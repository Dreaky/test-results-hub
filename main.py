from app.core.repositories.test_run_repo import TestRunRepository
from app.core.repositories.test_case_repo import TestCaseRepository
from app.core.repositories.test_result_repo import TestResultRepository
from app.core.services.parse_junit_results import load_test_cases_from_file
from app.core.services.report_service import ReportService
from app.infrastructure.minio_client import MinIOClient
import uuid
from pprint import pprint


# Generate valid UUIDs for run, test case, and test result
def generate_uuids():
    return {
        'run_id': str(uuid.uuid4()),  # Test run ID
        'tc_id': str(uuid.uuid4()),  # Test case ID
        'test_result_id': str(uuid.uuid4())  # Test result ID
    }


def process_and_insert_results(input_file):
    # Load the test cases from the XML file
    results = load_test_cases_from_file(input_file)
    pprint(results)
    


    # Insert results into the database using the service layer
    report_service = ReportService()
    report_service.upload_test_results(results)


if __name__ == '__main__':
    # Define the path to your JUnit XML result file
    input_junit = 'results-abis.xml'  # Provide path to your JUnit XML result file

    # Process and insert results into the database
    process_and_insert_results(input_junit)

    # Insert test data (this is separate from the result parsing)
    # insert_test_data()
