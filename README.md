# 🧪 Test Results Hub  

**Test Results Hub** is a lightweight and efficient reporting tool designed to collect, store, and visualize test execution results. It focuses on capturing only **failed test cases**, optimizing storage and performance. The system integrates with **JUnit test reports**, **MinIO for storage**, and **Grafana for visualization**.  

## 🚀 Features  
✅ **Test Failure Tracking** – Stores only failed test cases to minimize storage usage  
✅ **Performance Optimized** – Uses efficient data structures for fast query execution  
✅ **Database-Driven** – Supports PostgreSQL/MySQL for structured reporting  
✅ **MinIO Integration** – Saves full test reports in cloud storage  
✅ **Grafana Dashboard** – Provides real-time test analytics & failure histograms  
✅ **CI/CD Ready** – Works with Jenkins, GitHub Actions, and other pipelines  

---

## 🛠️ Tech Stack  

| Component            | Technology                            |
|----------------------|---------------------------------------|
| **Backend**          | Python (FastAPI) / Java (Spring Boot) |
| **Database**         | PostgreSQL / MySQL                    |
| **Storage**          | MinIO (S3-compatible)                 |
| **Data Parsing**     | JUnit XML Parser                      |
| **Visualization**    | Grafana                               |
| **Containerization** | Docker & Docker Compose               |

---

## 🏠 Project Structure  

```
test-results-hub/
│── src/                # Application source code
│   ├── api/            # REST API Endpoints
│   ├── db/             # Database models & queries
│   ├── minio/          # MinIO storage handling
│   ├── parsers/        # JUnit XML Parser
│   ├── services/       # Business logic & processing
│── grafana/            # Grafana configuration & dashboards
│── scripts/            # Utility scripts for setup
│── tests/              # Unit & integration tests
│── docker-compose.yml  # Docker setup
│── .env.example        # Environment variables template
│── README.md           # Project documentation
```

---

## 🛠️ Setup Instructions  

### **1️⃣ Prerequisites**  
Ensure you have the following installed:  
- **Docker & Docker Compose**  
- **Python 3.9+** (if using FastAPI) or **Java 17+** (if using Spring Boot)  
- **PostgreSQL or MySQL**  
- **MinIO (S3-compatible storage)**  
- **Grafana**  

---

### **2️⃣ Installation**  

Clone the repository:  
```bash
git clone https://github.com/your-username/test-results-hub.git
cd test-results-hub
```

Set up environment variables:  
```bash
cp .env.example .env
```
Modify `.env` with your database & MinIO credentials.

---

### **3️⃣ Start Services**  

Using Docker Compose:  
```bash
docker-compose up -d
```
This will start the database, MinIO, and Grafana.

Alternatively, run services manually:  
```bash
# Start PostgreSQL
docker run --name test-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=pass -d postgres

# Start MinIO
docker run --name minio -e MINIO_ACCESS_KEY=access -e MINIO_SECRET_KEY=secret -d minio/minio server /data
```

---

### **4️⃣ Import Grafana Dashboards**  

1. Open Grafana at `http://localhost:3000/`  
2. Login (default: `admin/admin`)  
3. Import the JSON dashboard from `grafana/dashboards/`  

---

## 📊 Grafana Dashboards  

📌 **Test Failure Histogram** – Most frequently failing tests  
📌 **Failure Trends** – See test pass/fail trends over time  
📌 **CI/CD Integration** – Identify flaky tests in automated pipelines  

---

## 🛠️ API Endpoints  

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/tests/upload` | Upload JUnit XML test results |
| `GET`  | `/api/tests/failures` | Fetch failed test cases |
| `GET`  | `/api/tests/histogram` | Get failure statistics |

Example API call:  
```bash
curl -X POST http://localhost:8000/api/tests/upload -F "file=@test-results.xml"
```

---

## 🚀 CI/CD Integration  

### **GitHub Actions Example**
```yaml
name: Run Tests & Upload Results
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Run Tests
        run: mvn test | tee test-results.xml

      - name: Upload to Test Results Hub
        run: curl -X POST http://your-api-url/api/tests/upload -F "file=@test-results.xml"
```

---

## 🐝 License  

This project is licensed under the GNU GENERAL PUBLIC License.  

---

## 🤝 Contributing  

Contributions are welcome! Please follow the guidelines:  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit changes (`git commit -m "Add feature xyz"`)  
4. Open a Pull Request