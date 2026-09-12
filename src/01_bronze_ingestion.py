# In a real Databricks environment, this script runs 24/7 reading from a stream like Kafka.
# spark.readStream.format("kafka")... 

print("Simulating streaming IoT data from vehicles and hospitals landing in Bronze...")

# Mocking the raw data landing in the Bronze table
# In production, Databricks Auto Loader handles this automatically.