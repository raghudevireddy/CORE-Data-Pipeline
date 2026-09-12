from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when

spark = SparkSession.builder.appName("CORE_Gold").getOrCreate()

# Mocking the DataFrames that would normally be read from Silver Delta tables
silver_fleet = spark.createDataFrame([
    ("VEH_001", "ACTIVE", 95),  # Full O2
    ("VEH_002", "ACTIVE", 10)   # Empty O2
], ["vehicle_id", "status", "o2_level"])

hospital_requests = spark.createDataFrame([("HOSP_A", "CRITICAL", "28262")], ["hospital_id", "hospital_urgency", "zipcode"])
weather_data = spark.createDataFrame([("28205", 185)], ["airnow_zipcode", "aqi"])

# The C.O.R.E. Priority Logic:
# 1. CRITICAL hospital + O2 > 20% = Emergency Delivery
# 2. O2 > 95% = Standard Delivery
# 3. Otherwise = Go purify high AQI zones
gold_routes = silver_fleet.crossJoin(hospital_requests).crossJoin(weather_data).withColumn(
    "assigned_task",
    when(
        (col("hospital_urgency") == "CRITICAL") & (col("o2_level") > 20), 
        lit("EMERGENCY_O2_DELIVERY")
    ).when(
        col("o2_level") >= 95, 
        lit("STANDARD_O2_DELIVERY")
    ).otherwise(
        lit("PURIFY_AIR_HIGH_AQI")
    )
).withColumn(
    "destination",
    when(
        (col("hospital_urgency") == "CRITICAL") & (col("o2_level") > 20), 
        col("hospital_id")
    ).otherwise(
        col("airnow_zipcode")
    )
).select("vehicle_id", "o2_level", "assigned_task", "destination")

print("\n--- FINAL ROUTING ASSIGNMENTS ---")
gold_routes.show()