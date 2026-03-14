# aws-serverless-travel-data-pipeline
# 🚍 Travel Data Pipeline (AWS Data Engineering Project)
 
 ## 📌 Project Overview

This project demonstrates an **end-to-end serverless data pipeline** built on AWS.
The pipeline ingests travel route pricing data from a custom API, stores raw data in an **Amazon S3 data lake**, automatically triggers processing using **AWS Lambda and AWS Glue (PySpark)**, and generates analytics-ready datasets for dashboards.

The objective of this project is to showcase **data ingestion, ETL processing, and cloud-based data lake architecture** used in modern data engineering workflows.

---

# 🏗 Architecture

```
Flask API
   ↓
Python Collector Script
   ↓
Amazon S3 (Raw Layer)
   ↓
S3 Event Trigger
   ↓
AWS Lambda
   ↓
AWS Glue ETL (PySpark)
   ↓
Amazon S3 (Processed Layer)
```

---

# ⚙️ Technologies Used

| Layer              | Technology               |
| ------------------ | ------------------------ |
| Data Generation    | Python, Flask            |
| Data Ingestion     | Python (Requests, Boto3) |
| Storage            | Amazon S3                |
| Event Trigger      | S3 Event Notifications   |
| Serverless Compute | AWS Lambda               |
| ETL Processing     | AWS Glue (PySpark)       |
| Data Lake          | Amazon S3                |
| Visualization      | Excel / Power BI         |

---

# 📊 Dataset Description

The pipeline generates travel pricing data for **multiple routes across 60 days**.

### Dataset Fields

* Source
* Destination
* Date
* Time
* Contact Number
* Duration
* Rating
* Seat Type
* Status
* Lowest Price
* Highest Price
* Average Price

### Records Generated

```
8 Routes × 60 Days = 480 Records
```

Each API call generates a **complete dataset of 480 travel pricing records**.

---

# 📁 Project Structure

```
travel-data-pipeline
│
├── api
│   └── travel_api.py
│
├── ingestion
│   └── collector.py
│
├── glue
│   └── travel_etl.py
│
├── architecture
│   └── pipeline_architecture.png
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Pipeline Workflow

### Step 1 — API Data Generation

A Flask API generates synthetic travel pricing data.

```
python api/travel_api.py
```

Endpoint:

```
http://127.0.0.1:5000/traveldata
```

The API produces **480 travel records** for analysis.

---

### Step 2 — Data Ingestion

The collector script fetches the API data and uploads it to **Amazon S3 Raw Layer**.

```
python ingestion/collector.py
```

Data format stored in S3:

```
JSON Lines
```

---

### Step 3 — Raw Data Storage

Data is stored in the S3 data lake:

```
s3://travel-data-lake/raw/
```

Example file:

```
travel_20260311_183000.json
```

---

### Step 4 — Automated Event Trigger

When a new file is uploaded:

```
S3 Event Trigger
      ↓
AWS Lambda
      ↓
Start Glue Job
```

---

### Step 5 — ETL Processing

AWS Glue runs a **PySpark ETL job** that:

1. Reads raw JSON files from S3
2. Processes and structures the dataset
3. Writes the output as CSV files

Processed data location:

```
s3://travel-data-lake/processed/
```

---

### Step 6 — Processed Dataset

Output file:

```
part-0000.csv
```

Example structure:

```
Source,Destination,Date,Time,Lowest,Highest,Average
Pune,Mumbai,11-03-2026,05:00 AM,1800,2300,2050
Mumbai,Pune,11-03-2026,04:30 AM,1700,2100,1900
```

---

# 📈 Use Cases

This pipeline simulates real-world travel pricing analytics systems used by platforms such as:

* RedBus
* MakeMyTrip
* Uber
* Airline booking systems

Possible business insights:

* Route price trends
* Demand-based price changes
* Historical travel pricing analysis
* Dashboard reporting

---

# 🧠 Data Engineering Concepts Demonstrated

This project demonstrates key **data engineering principles**:

* Data Ingestion from APIs
* Cloud Data Lake Architecture
* Event-Driven Pipelines
* Serverless Processing
* ETL using PySpark
* Automated Data Pipelines

---

# 🔧 Installation

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🖥 How to Run the Project

Start the API server:

```
python api/travel_api.py
```

Run the data ingestion script:

```
python ingestion/collector.py
```

The pipeline will automatically process data using **Lambda and Glue**.

---

# 📷 Sample Output

Processed dataset stored in:

```
S3 → travel-data-lake/processed/
```

Output contains **480 structured records** ready for analytics dashboards.

---

# 👨‍💻 Author

**Krushna Dode**

Data Engineering | Python | AWS | PySpark | SQL

GitHub:
https://github.com/Krushnadode-80


# ⭐ Future Improvements

* Convert data format to **Parquet for faster analytics**
* Query data using **AWS Athena**
* Build **real-time dashboards**
* Implement **data partitioning**
* Add **CI/CD pipeline**
