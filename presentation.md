# Implementation of Energy Optimization Goals

## 1. Identifier des opportunités d'optimisation énergétique (Identifying Energy Optimization Opportunities)

### Implementation:
- Created real-time energy consumption monitoring system using:
  ```python
  def generate_recommendations(df):
      return df.withColumn("recommendations",
          when((col("hour_of_day").between(9, 17)) & (col("avg_consumption") > 150),
              "High consumption during peak hours...") \
          .when((col("temperature") > 25) & (col("avg_consumption") > 130),
              "High energy use with high temperature...") \
          .when((col("occupancy") < 30) & (col("avg_consumption") > 100),
              "High energy use with low occupancy..."))
  ```

### Key Features:
1. **Peak Hours Detection**
   - Monitors consumption between 9 AM - 5 PM
   - Flags high consumption periods (>150 kWh)

2. **Temperature Correlation**
   - Analyzes relationship between temperature and energy use
   - Identifies inefficient cooling patterns

3. **Occupancy Analysis**
   - Tracks energy usage vs. building occupancy
   - Highlights waste during low-occupancy periods

## 2. Proposer des recommandations basées sur les résultats de l'analyse (Proposing Analysis-Based Recommendations)

### Implementation:
```python
def calculate_peak_hours_impact(df):
    return df \
        .withColumn("cost_impact", 
            when(col("is_peak_hour") == "Peak", col("avg_consumption") * 1.5)
            .otherwise(col("avg_consumption"))) \
        .withColumn("potential_savings",
            when(col("is_peak_hour") == "Peak", 
                (col("avg_consumption") * 1.5) - (col("avg_consumption") * 0.8))
            .otherwise(0))
```

### Recommendations Generated:
1. **Peak Hours Optimization**
   - HVAC setting adjustments
   - Task scheduling for off-peak hours
   - Automated lighting controls

2. **Temperature-Based Recommendations**
   - Cooling system optimization
   - Solar shading installation
   - Natural ventilation strategies

3. **Occupancy-Based Solutions**
   - Motion sensor implementation
   - Base load reduction
   - Always-on equipment auditing

## 3. Simuler la provenance de données en temps réels (Simulating Real-Time Data)

### Implementation:
```python
def create_energy_data():
    data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'building_id': random.randint(1, 10),
        'energy_consumption': random.uniform(50, 200),
        'temperature': random.uniform(15, 35),
        'humidity': random.uniform(30, 80),
        'occupancy': random.randint(0, 100)
    }
    return data
```

### Technology Stack:
1. **Apache Kafka**
   - Real-time data streaming
   - Message queuing
   - Data distribution

2. **Apache Spark Streaming**
   - Real-time data processing
   - Window-based analytics
   - Continuous recommendations

### Data Flow:
1. Data Generator → Kafka Topic
2. Spark Streaming ← Kafka Topic
3. Analysis & Recommendations
4. Storage in HDFS

## Results and Visualization

### Real-Time Monitoring:
- Access Jupyter Lab: http://localhost:8888 (token: admin)
- View live data streams
- Monitor recommendations

### Analysis Output:
```
+------------------+------------+-----------------+------------------+
| window           | building_id| avg_consumption | recommendations  |
+------------------+------------+-----------------+------------------+
| 2025-01-20 14:55 |     1     |     175.5      | High consumption |
| 2025-01-20 15:00 |     2     |     120.3      | Normal levels    |
+------------------+------------+-----------------+------------------+
```

## Testing the Implementation

1. **View Raw Data**:
   ```bash
   docker-compose exec kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic energy_data
   ```

2. **Monitor Analysis**:
   ```bash
   docker-compose exec jupyter python work/scripts/energy_optimization_analysis.py
   ```

3. **Access Results**:
   - Real-time console output
   - HDFS storage for historical analysis
   - Jupyter notebooks for custom analysis
