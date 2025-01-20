from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import json

def create_spark_session():
    """Create Spark session with necessary configurations"""
    return SparkSession.builder \
        .appName("Energy Optimization Analysis") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
        .getOrCreate()

def define_schema():
    """Define schema for energy data"""
    return StructType([
        StructField("timestamp", StringType(), True),
        StructField("building_id", IntegerType(), True),
        StructField("energy_consumption", DoubleType(), True),
        StructField("temperature", DoubleType(), True),
        StructField("humidity", DoubleType(), True),
        StructField("occupancy", IntegerType(), True),
        StructField("day_of_week", IntegerType(), True),
        StructField("hour_of_day", IntegerType(), True)
    ])

def generate_recommendations(df):
    """Generate energy optimization recommendations based on analysis"""
    return df \
        .withColumn("recommendations",
            when((col("hour_of_day").between(9, 17)) & (col("avg_consumption") > 150),
                "High consumption during peak hours: 1) Adjust HVAC settings 2) Schedule high-energy tasks for off-peak hours 3) Implement automated lighting controls") \
            .when((col("temperature") > 25) & (col("avg_consumption") > 130),
                "High energy use with high temperature: 1) Optimize cooling system efficiency 2) Install solar shading 3) Use natural ventilation when possible") \
            .when((col("occupancy") < 30) & (col("avg_consumption") > 100),
                "High energy use with low occupancy: 1) Implement motion sensors 2) Reduce base load 3) Audit always-on equipment") \
            .otherwise("Energy consumption within normal parameters"))

def calculate_peak_hours_impact(df):
    """Calculate impact of peak hours on energy consumption"""
    return df \
        .withColumn("is_peak_hour", 
            when(col("hour_of_day").between(9, 17), "Peak").otherwise("Off-Peak")) \
        .withColumn("cost_impact", 
            when(col("is_peak_hour") == "Peak", col("avg_consumption") * 1.5)
            .otherwise(col("avg_consumption"))) \
        .withColumn("potential_savings",
            when(col("is_peak_hour") == "Peak", 
                (col("avg_consumption") * 1.5) - (col("avg_consumption") * 0.8))
            .otherwise(0))

def process_energy_data(spark):
    """Process streaming energy data and perform analysis"""
    
    # Read streaming data from Kafka
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("subscribe", "energy_data") \
        .load()
    
    # Parse JSON data
    parsed_df = df.select(
        from_json(col("value").cast("string"), define_schema()).alias("data")
    ).select("data.*")
    
    # Calculate real-time metrics
    metrics_df = parsed_df \
        .withWatermark("timestamp", "1 minute") \
        .groupBy(
            window("timestamp", "5 minutes"),
            "building_id",
            "hour_of_day"
        ) \
        .agg(
            avg("energy_consumption").alias("avg_consumption"),
            max("energy_consumption").alias("peak_consumption"),
            avg("temperature").alias("temperature"),
            avg("humidity").alias("humidity"),
            avg("occupancy").alias("occupancy")
        )
    
    # Add recommendations and impact analysis
    analysis_df = metrics_df \
        .transform(generate_recommendations) \
        .transform(calculate_peak_hours_impact)
    
    # Write results to console
    query = analysis_df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .option("truncate", False) \
        .start()
    
    # Write detailed analysis to HDFS
    hdfs_query = analysis_df \
        .select(
            "window",
            "building_id",
            "avg_consumption",
            "peak_consumption",
            "temperature",
            "humidity",
            "occupancy",
            "is_peak_hour",
            "cost_impact",
            "potential_savings",
            "recommendations"
        ) \
        .writeStream \
        .outputMode("append") \
        .format("parquet") \
        .option("path", "hdfs://hadoop-master:9000/data/energy_analysis") \
        .option("checkpointLocation", "hdfs://hadoop-master:9000/checkpoints") \
        .start()
    
    query.awaitTermination()
    hdfs_query.awaitTermination()

def main():
    spark = create_spark_session()
    process_energy_data(spark)

if __name__ == "__main__":
    main()
