# Spark Docker Environment

Docker-based Apache Spark 3.5.7 cluster with Jupyter notebooks support for data lake development (Delta Lake, Iceberg, Hudi).

## Requirements

- Docker
- Docker Compose
- Make (optional)

## Quick Start

```bash
# Start the cluster
make up
# or: docker compose up -d --build

# Access master container
make dev  
# or: docker exec -it spark-master bash

# Launch Jupyter notebook
cd /opt/spark/notebooks
jupyter notebook --no-browser --allow-root --ip=0.0.0.0 --port=8889
```

Find the Jupyter token in the output:
```
http://127.0.0.1:8889/tree?token=abc123...
```

## Web Interfaces

- **Spark Master UI**: http://localhost:8080
- **Spark History Server**: http://localhost:18080  
- **Jupyter Notebooks**: http://localhost:8889
- **Application UI**: http://localhost:4040 (when jobs are running)

## Usage Examples

### Connect to Spark Cluster
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .master("spark://spark-master:7077") \
    .getOrCreate()
```

### Run Demo Scripts
```bash
python scripts/delta-demo.py
python scripts/iceberg-demo.py  
python scripts/hudi-demo.py
```

## Data Lake Support

Pre-installed JAR libraries:
- **Delta Lake** 2.4.0/3.2.0
- **Apache Iceberg** 1.4.3
- **Apache Hudi** 0.15.0

## Stop Cluster

```bash
make down
# or: docker compose down --rmi all
```
