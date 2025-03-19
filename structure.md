test-reporting/
│── app/                     # Main application folder
│   ├── __init__.py
│   ├── config/               # Configuration files
│   │   ├── db_config.py      # Database connection setup
│   │   ├── minio_config.py   # MinIO connection setup
│   │   ├── settings.py       # General settings
│   ├── core/                 # Business logic
│   │   ├── repositories/     # Database repositories
│   │   │   ├── test_run_repo.py
│   │   │   ├── test_case_repo.py
│   │   │   ├── test_result_repo.py
│   │   ├── services/         # High-level services
│   │   │   ├── test_service.py
│   │   │   ├── report_service.py
│   ├── infrastructure/       # External services (DB, MinIO, logging)
│   │   ├── database.py       # Database initialization
│   │   ├── minio_client.py   # MinIO client
│   │   ├── logging_config.py # Logging configuration
│   ├── api/                  # Optional: REST API
│   │   ├── routes/
│   │   │   ├── test_routes.py
│   │   ├── app.py            # FastAPI app
│── tests/                    # Unit and integration tests
│   ├── test_services.py
│   ├── test_repositories.py
│── scripts/                   # Utility scripts
│   ├── init_db.py            # Script to initialize database
│── main.py                    # Entrypoint to run services
│── requirements.txt            # Dependencies
│── Dockerfile                  # Optional Docker setup
│── .env                        # Environment variables
│── README.md     