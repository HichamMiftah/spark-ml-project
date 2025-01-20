from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime, timedelta

def create_energy_data():
    """Generate simulated energy consumption data"""
    current_time = datetime.now()
    
    data = {
        'timestamp': current_time.strftime('%Y-%m-%d %H:%M:%S'),
        'building_id': random.randint(1, 10),
        'energy_consumption': random.uniform(50, 200),  # kWh
        'temperature': random.uniform(15, 35),  # Celsius
        'humidity': random.uniform(30, 80),  # Percentage
        'occupancy': random.randint(0, 100),  # Number of people
        'day_of_week': current_time.weekday(),
        'hour_of_day': current_time.hour
    }
    
    return data

def main():
    # Configure Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    print("Starting energy data generation...")
    
    while True:
        # Generate data
        energy_data = create_energy_data()
        
        # Send to Kafka topic
        producer.send('energy_data', energy_data)
        print(f"Sent data: {energy_data}")
        
        # Wait for 5 seconds before next data point
        time.sleep(5)

if __name__ == "__main__":
    # Wait for Kafka to be ready
    time.sleep(30)
    main()
