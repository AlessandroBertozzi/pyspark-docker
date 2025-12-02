# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Docker-based Apache Spark development environment that provides a complete local Spark cluster. The project is based on Spark 3.5.5 with Python 3.12.

## Architecture

The system consists of three main Docker containers:
- **spark-master**: The Spark master node that coordinates the cluster and provides the WebUI
- **spark-worker**: Worker nodes that execute Spark tasks
- **spark-history-server**: Provides historical job information and logs

All containers share common volumes for notebooks and logs, enabling seamless data sharing and persistence.

## Core Components

- **Dockerfile**: Multi-stage build creating Spark environment
- **docker-compose.yml**: Orchestrates the complete Spark cluster
- **entrypoint.sh**: Container startup script that configures master/worker/history roles
- **conf/spark-defaults.conf**: Spark cluster configuration
- **notebooks/**: Jupyter notebooks directory

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

# Launch Jupyter notebooks
cd /opt/spark/notebooks
jupyter notebook --no-browser --allow-root --ip=0.0.0.0 --port=8889
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
- **Configuration**: Uses Delta catalog extensions

### Apache Iceberg
- **JAR**: `iceberg-spark-runtime-3.4_2.12:1.4.3`
- **Configuration**: Uses Hadoop catalog

### Apache Hudi
- **JAR**: `hudi-spark3-bundle_2.12:0.15.0`
- **Configuration**: Uses Hudi catalog with Kryo serialization

## Development Notes

- All containers run as root user (consider security implications for production)
- Python dependencies are managed in `requirements.txt`
- Spark configuration is centralized in `conf/spark-defaults.conf`
- Event logging is enabled and stored in `/opt/spark/spark-events`

## File Structure
```
conf/            # Spark configuration files
notebooks/       # Jupyter notebooks
spark-logs/      # Spark event logs for history server
```

## Testing Environment

To test the environment setup:
1. Start cluster with `make up`
2. Access master node with `make dev`
3. Start PySpark shell: `pyspark`
4. Create a simple DataFrame and verify cluster operation
5. Check Spark UI to see job execution details