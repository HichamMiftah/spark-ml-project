# Spark ML Project with Jupyter Lab

This project sets up a complete environment for machine learning with Apache Spark, including:
- Apache Spark cluster (master and worker)
- Apache Hadoop (namenode and datanode)
- Jupyter Lab with PySpark support

## Prerequisites
- Docker
- Docker Compose

## Quick Start

1. Clone the repository:
```bash
git clone git@github.com:HichamMiftah/spark-ml-project.git
cd spark-ml-project
```

2. Start the services:
```bash
docker-compose up -d
```

3. Access the services:
- Jupyter Lab: http://localhost:8888 (token: admin)
- Spark Master UI: http://localhost:8080
- Hadoop UI: http://localhost:9870

## Project Structure
```
.
├── data/               # Data directory mounted to containers
├── notebooks/          # Jupyter notebooks directory
├── docker-compose.yml  # Docker compose configuration
└── README.md          # This file
```

## Services

### Jupyter Lab
- Port: 8888
- Working directory: /home/jovyan/work
- Data directory: /data
- Spark connection: spark://spark-master:7077

### Apache Spark
- Master port: 7077
- Master UI port: 8080
- Worker with 1G memory and 1 core

### Apache Hadoop
- Namenode port: 9000
- Namenode UI port: 9870
- Datanode for distributed storage

## Development

1. Create new notebooks in Jupyter Lab
2. Access your data through the mounted `/data` directory
3. Use PySpark with the preconfigured Spark master

## Notes
- The Jupyter Lab token is set to: `admin`
- Spark Worker is configured with 1G memory and 1 core
- Data persistence is handled through Docker volumes
