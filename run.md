# Running Guide for Energy Optimization Project

## Prerequisites
1. Make sure Docker and Docker Compose are installed
2. Clone the repository:
   ```bash
   git clone https://github.com/HichamMiftah/spark-ml-project.git
   cd spark-ml-project
   ```

## Starting the Environment
```bash
# Start required services
docker-compose up -d kafka jupyter

# Wait for services to be ready (about 30 seconds)
docker-compose ps
```

---

## Goal 1: Identifier des opportunités d'optimisation énergétique
> Identifying energy optimization opportunities through real-time monitoring

### Running the Analysis
```bash
# Start the energy optimization analysis
docker-compose exec jupyter python work/scripts/energy_optimization_analysis.py
```

### What to Look For
- Watch the console output for:
  ```
  +------------------+------------+-----------------+
  | window           | building_id| avg_consumption |
  +------------------+------------+-----------------+
  ```
- The analysis will show:
  - Peak consumption periods
  - Temperature correlations
  - Occupancy patterns

---

## Goal 2: Proposer des recommandations basées sur les résultats de l'analyse
> Providing recommendations based on analysis results

### Viewing Recommendations
```bash
# The recommendations are part of the analysis output
# They will appear in the console as:
```
Example output:
```
+------------------+------------------+
| situation        | recommendation   |
+------------------+------------------+
| Peak Hours       | 1) Adjust HVAC   |
|                  | 2) Schedule tasks|
+------------------+------------------+
```

### Types of Recommendations
1. **Peak Hours (9 AM - 5 PM)**
   ```bash
   # Look for entries with:
   "High consumption during peak hours: 1) Adjust HVAC settings..."
   ```

2. **Temperature-Based**
   ```bash
   # Look for entries with:
   "High energy use with high temperature: 1) Optimize cooling system..."
   ```

3. **Occupancy-Based**
   ```bash
   # Look for entries with:
   "High energy use with low occupancy: 1) Implement motion sensors..."
   ```

---

## Goal 3: Simuler la provenance de données en temps réels
> Simulating real-time data using Apache Kafka and Spark Streaming

### 1. Start Data Generation
```bash
# Run the data generator
docker-compose exec -d jupyter python work/scripts/energy_data_generator.py
```

### 2. View Raw Data Stream
```bash
# Monitor Kafka messages
docker-compose exec kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic energy_data --from-beginning
```

### 3. Monitor Complete System
```bash
# Terminal 1 - Raw data
docker-compose exec kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic energy_data

# Terminal 2 - Analysis and recommendations
docker-compose exec jupyter python work/scripts/energy_optimization_analysis.py
```

---

## Additional Analysis Tools

### Jupyter Lab Interface
1. Access Jupyter Lab:
   - Open browser: http://localhost:8888
   - Token: admin

2. Navigate to work directory:
   - You'll find the scripts in the `scripts` folder
   - Data analysis notebooks can be created here

### Monitoring Tools
```bash
# Check service status
docker-compose ps

# View service logs
docker-compose logs -f jupyter
docker-compose logs -f kafka
```

### Stopping the System
```bash
# Stop all services
docker-compose down

# To also remove volumes
docker-compose down -v
```

## Troubleshooting

### If Data Generator Isn't Working
```bash
# Restart the data generator
docker-compose restart jupyter
docker-compose exec -d jupyter python work/scripts/energy_data_generator.py
```

### If Analysis Isn't Showing
```bash
# Check Kafka topics
docker-compose exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092

# Restart analysis
docker-compose exec jupyter python work/scripts/energy_optimization_analysis.py
```

### Common Issues
1. **No Data Flowing**
   ```bash
   # Verify Kafka topic exists
   docker-compose exec kafka kafka-topics.sh --describe --topic energy_data --bootstrap-server localhost:9092
   ```

2. **Analysis Errors**
   ```bash
   # Check Python dependencies
   docker-compose exec jupyter pip list | grep -E "kafka-python|pyspark"
   ```

3. **Service Health**
   ```bash
   # Check service health
   docker-compose ps
   ```
