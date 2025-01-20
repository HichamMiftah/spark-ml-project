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

## Testing the Project

### Using Jupyter Notebook
We provide a comprehensive Jupyter notebook for testing all aspects of the project:

1. Access Jupyter Lab:
   ```bash
   # The notebook is available at http://localhost:8888
   # Token: admin
   ```

2. Navigate to `notebooks/energy_optimization_test.ipynb`

3. Test each goal:
   - Goal 1: Energy optimization identification
   - Goal 2: Automated recommendations
   - Goal 3: Real-time data simulation

### Test Scenarios
The notebook includes various test scenarios:
- Peak hour consumption (9 AM - 5 PM)
- High temperature scenarios
- Low occupancy situations
- Real-time data simulation

### Documentation
For more detailed information, see:
- `run.md`: Step-by-step running instructions
- `presentation.md`: Project presentation and implementation details

## Project Goals

1. **Identifier des opportunités d'optimisation énergétique**
   - Real-time energy consumption monitoring
   - Peak hours detection (9 AM - 5 PM)
   - Temperature correlation analysis
   - Occupancy pattern recognition

2. **Proposer des recommandations**
   - HVAC optimization suggestions
   - Peak hour load management
   - Temperature-based recommendations
   - Occupancy-based energy saving tips

3. **Simuler la provenance de données en temps réels**
   - Kafka-based real-time data streaming
   - Random data generation with realistic patterns
   - Multiple building simulation
   - Various environmental conditions

## Notes
- The Jupyter Lab token is set to: `admin`
- Spark Worker is configured with 1G memory and 1 core
- Data persistence is handled through Docker volumes
