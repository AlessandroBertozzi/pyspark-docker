# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Docker-based Apache Spark development environment that provides a complete local Spark cluster with support for modern data lake formats including Delta Lake, Apache Iceberg, and Apache Hudi. The project is based on Spark 3.5.5 with Python 3.12.

## Architecture

The system consists of three main Docker containers:
- **spark-master**: The Spark master node that coordinates the cluster and provides the WebUI
- **spark-worker**: Worker nodes that execute Spark tasks
- **spark-history-server**: Provides historical job information and logs

All containers share common volumes for scripts, data, logs, and warehouse storage, enabling seamless data sharing and persistence.

## Core Components

- **Dockerfile**: Multi-stage build creating Spark environment with data lake libraries pre-installed
- **docker-compose.yml**: Orchestrates the complete Spark cluster
- **entrypoint.sh**: Container startup script that configures master/worker/history roles
- **scripts/**: Collection of demo scripts showcasing different data lake technologies
- **conf/spark-defaults.conf**: Spark cluster configuration
- **data/**: Input data directory
- **warehouse/**: Data warehouse storage for tables

## Common Development Commands

### Cluster Management
```bash
# Start the Spark cluster
make up
# or manually: docker compose up -d --build

# Stop the cluster and clean up
make down
# or manually: docker compose down --rmi all

# Access the master node interactive shell
make dev
# or manually: docker exec -it spark-master bash
```

### Development Workflow
```bash
# Start PySpark shell inside master container
pyspark

# Run a specific demo script
python scripts/delta-demo.py
python scripts/iceberg-demo.py
python scripts/hudi-demo.py
```

### Web Interfaces
- Spark Master UI: http://localhost:8080
- Spark History Server: http://localhost:18080
- Application UI: http://localhost:4040 (when running jobs)
- Jupyter (if enabled): http://localhost:8889

## Data Lake Technologies

The environment comes pre-configured with JAR files and dependencies for:

### Delta Lake
- **JAR**: `delta-core_2.12:2.4.0`, `delta-spark_2.12:3.2.0`, `delta-storage:3.2.0`
- **Demo script**: `scripts/delta-demo.py`, `scripts/delta-cdc.py`
- **Configuration**: Uses Delta catalog extensions

### Apache Iceberg
- **JAR**: `iceberg-spark-runtime-3.4_2.12:1.4.3`
- **Demo script**: `scripts/iceberg-demo.py`, `scripts/iceberg-load.py`
- **Configuration**: Uses Hadoop catalog with warehouse in `./warehouse`

### Apache Hudi
- **JAR**: `hudi-spark3-bundle_2.12:0.15.0`
- **Demo script**: `scripts/hudi-demo.py`
- **Configuration**: Uses Hudi catalog with Kryo serialization

## Script Examples

Each demo script follows a similar pattern:
1. Configure SparkSession with appropriate extensions and catalogs
2. Create sample data with defined schema
3. Write data to the respective table format
4. Demonstrate read operations and format-specific features
5. Show table metadata and time travel capabilities (where supported)

## Development Notes

- All containers run as root user (consider security implications for production)
- Python dependencies are managed in `requirements.txt`
- Spark configuration is centralized in `conf/spark-defaults.conf`
- Event logging is enabled and stored in `/opt/spark/spark-events`
- The warehouse directory persists table metadata and data files

## File Structure
```
scripts/          # Demo and example PySpark scripts
conf/            # Spark configuration files
data/            # Input data directory
warehouse/       # Table storage (Delta, Iceberg, Hudi tables)
spark-logs/      # Spark event logs for history server
```

## Testing Scripts

To test the environment setup:
1. Start cluster with `make up`
2. Access master node with `make dev`
3. Run any demo script: `python scripts/delta-demo.py`
4. Verify tables are created in the warehouse directory
5. Check Spark UI to see job execution details