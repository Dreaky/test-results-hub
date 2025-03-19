from test_run_repo import TestRunRepository
from test_case_repo import TestCaseRepository
from test_result_repo import TestResultRepository
from minio_repo import MinIORepository

# Example usage
run_id = "1234"
tc_id = "T001"

# Insert test run
TestRunRepository.insert_test_run(run_id, "Regression Suite", "Postgres", "Linux", "2025-03-19", "v1.2")

# Insert test case
TestCaseRepository.insert_test_case(tc_id, "Login Test", "QA Team", "http://jira.com/bug123", "T001", "Web App")

# Upload report to MinIO
report_url = MinIORepository.upload_report("report_1234.html")

# Insert failed test
TestResultRepository.insert_failed_test("5678", tc_id, run_id, "FAILED", 15.3, "Regression", "AssertionError", report_url)
