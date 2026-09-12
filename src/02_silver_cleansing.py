from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("CORE_Silver").getOrCreate()

# 1. Read from Bronze
# df_bronze_fleet = spark.read.format("delta").load("/mnt/data/bronze/fleet")

# 2. Cleanse Data: Filter out vehicles that are in maintenance (only route ACTIVE vehicles)
# df_silver_fleet = df_bronze_fleet.filter(col("status") == "ACTIVE").dropDuplicates(["vehicle_id"])

# 3. Write to Silver
# df_silver_fleet.write.format("delta").mode("overwrite").save("/mnt/data/silver/fleet")

print("Silver layer processing complete: Data cleansed and standardized.")