import requests
import boto3
import json
from datetime import datetime
import os

url = "http://127.0.0.1:5000/traveldata"

response = requests.get(url)
data = response.json()

file_name = f"travel_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

# JSON Lines format
with open(file_name, "w") as f:
    for record in data:
        f.write(json.dumps(record) + "\n")

s3 = boto3.client("s3")

bucket = "travel-data-lake"

s3.upload_file(file_name, bucket, f"raw/{file_name}")
os.remove(file_name)

print("Uploaded 480 rows to raw/")