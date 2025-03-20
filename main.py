from app.core.services.parse_junit_results import load_test_cases_from_file
from app.core.services.report_service import ReportService


def process_and_insert_results(input_file):
    # Load the test cases from the XML file
    results = load_test_cases_from_file(input_file)
    # Insert results into the database using the service layer
    report_service = ReportService()
    report_service.upload_test_results(results)


if __name__ == '__main__':
    # Define the path to your JUnit XML result file
    input_junit = 'results-abis_f.xml'

    # Process and insert results into the database
    process_and_insert_results(input_junit)
