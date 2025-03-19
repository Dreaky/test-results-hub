## Test Results Hub  

### 📌 Overview  
`test-results-hub` is a lightweight and efficient reporting tool designed to collect, store, and visualize test execution results. It focuses on capturing only **failed test cases**, optimizing storage and performance. The system integrates with **JUnit test reports**, **MinIO for storage**, and **Grafana for visualization**.  

### 🎯 Key Features  
✅ **Test Failure Tracking** – Stores only failed test cases to minimize storage usage  
✅ **Performance Optimized** – Uses efficient data structures for fast query execution  
✅ **Database-Driven** – Supports PostgreSQL/MySQL for structured reporting  
✅ **MinIO Integration** – Saves full test reports in cloud storage  
✅ **Grafana Dashboard** – Provides real-time test analytics & failure histograms  
✅ **CI/CD Ready** – Works with Jenkins, GitHub Actions, and other pipelines  

### 🛠️ Tech Stack  
- **Database:** PostgreSQL / MySQL  
- **Storage:** MinIO (S3-compatible)  
- **Backend:** Python (FastAPI / Flask) or Java (Spring Boot)  
- **Data Processing:** JUnit XML parser  
- **Visualization:** Grafana  

### 📊 Expected Dashboards in Grafana  
📌 Test Failure Histogram – Most frequently failing tests  
📌 Failure Trends – See test pass/fail trends over time  
📌 CI/CD Integration – Identify flakiness in automated pipelines  

### 🚀 Next Steps
- Setup repository structure (`/src`, `/db`, `/grafana`, etc.)  
- Create DB schema & MinIO storage handling  
- Integrate JUnit XML parsing  
- Build APIs for querying test failures  
- Configure Grafana dashboards  

This repo aims to provide **clear insights into test failures** for better debugging and quality assurance! 🔍  

---
## **🚀 Running the Application**
### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2️⃣ Initialize the Database**
```bash
python scripts/init_db.py
```

### **3️⃣ Run FastAPI Server**
```bash
uvicorn app.api.app:app --host 0.0.0.0 --port 8000 --reload
```

### **4️⃣ Send Test Data via API**
```bash
curl -X POST "http://localhost:8000/report_failed_test" -H "Content-Type: application/json" -d '
{
    "run_id": "1234",
    "tc_id": "T001",
    "status": "FAILED",
    "elapsed": 15.3,
    "tag": "Regression",
    "notes": "AssertionError: Expected 200, got 500",
    "report_path": "report_1234.html"
}'
```

---

## **📊 Grafana Integration**
### **1️⃣ Connect PostgreSQL to Grafana**
1. Open Grafana  
2. Add **PostgreSQL Data Source**  
3. Configure with:
   - Host: `localhost`
   - Database: `test_db`
   - User: `test_user`
4. Click **Save & Test**

### **2️⃣ Create Dashboard for Failures**
- Go to **Dashboards > New Panel**  
- Use SQL Query:
```sql
SELECT tag, COUNT(*) AS failures 
FROM test_result 
WHERE status = 'FAILED' 
GROUP BY tag 
ORDER BY failures DESC;
```
- Select **Bar Chart Visualization**  
- Save Dashboard ✅