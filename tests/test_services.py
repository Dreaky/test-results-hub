from app.core.tables.test_results import TestResultTable
from app.infrastructure.minio_client import MinIOClient


class TestService:
    @staticmethod
    def process_failed_test(run_id, tc_id, test_status, elapsed, tag, notes, report_path):
        if test_status == "FAILED":
            report_url = MinIOClient.upload_report(report_path)
            TestResultTable.insert_failed_test(
                result_id="5678", tc_id=tc_id, run_id=run_id,
                status="FAILED", elapsed_time=elapsed, tag=tag,
                notes=notes, report_url=report_url
            )
