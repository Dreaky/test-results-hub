import boto3
from app.config.settings import MINIO_CONFIG

s3 = boto3.client("s3", endpoint_url=MINIO_CONFIG["url"],
                  aws_access_key_id=MINIO_CONFIG["access_key"],
                  aws_secret_access_key=MINIO_CONFIG["secret_key"])


class MinIOClient:
    @staticmethod
    def upload_report(file_path, bucket_name="test-reports"):
        with open(file_path, "rb") as f:
            s3.upload_fileobj(f, bucket_name, file_path.split("/")[-1])
        return f"{MINIO_CONFIG['url']}/{bucket_name}/{file_path.split('/')[-1]}"
