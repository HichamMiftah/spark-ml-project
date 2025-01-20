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
            "building_id"
        ) \
        .agg(
            avg("energy_consumption").alias("avg_consumption"),
            max("energy_consumption").alias("peak_consumption"),
            avg("temperature").alias("avg_temperature"),
            avg("occupancy").alias("avg_occupancy")
        )
    
    # Identify optimization opportunities
    optimizations_df = metrics_df \
        .withColumn("optimization_needed",
            when(col("avg_consumption") > 150, "High consumption alert")
            .when(col("peak_consumption") > 180, "Peak demand alert")
            .otherwise("Normal")
        )
    
    # Write results to console (for testing)
    query = optimizations_df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .option("truncate", False) \
        .start()
    
    # Write results to HDFS
    hdfs_query = optimizations_df \
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
