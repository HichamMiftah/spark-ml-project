# Create directory in HDFS
docker-compose exec hadoop hdfs dfs -mkdir -p /data

# Copy the file
docker-compose exec hadoop hdfs dfs -put /data/Metro_Interstate_Traffic_Volume.csv /data/
