import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql import Row

# Initialize Spark (Databricks does this automatically, but good for local testing)
spark = SparkSession.builder.appName("CORE_Weather").getOrCreate()

# In production, use dbutils.secrets.get() instead of hardcoding
API_KEY = "YOUR_API_KEY_HERE" 
ZIP_CODE = "28262" 

url = f"https://www.airnowapi.org/aq/observation/zipCode/current/"
params = {
    "format": "application/json",
    "zipCode": ZIP_CODE,
    "distance": 25,
    "API_KEY": API_KEY
}

response = requests.get(url, params=params)

if response.status_code == 200 and len(response.json()) > 0:
    data = response.json()
    
    schema = StructType([
        StructField("DateObserved", StringType(), True),
        StructField("Latitude", DoubleType(), True),
        StructField("Longitude", DoubleType(), True),
        StructField("AQI", IntegerType(), True),
        StructField("Category_Name", StringType(), True)
    ])
    
    processed_rows = [Row(
        DateObserved=item.get("DateObserved"),
        Latitude=float(item.get("Latitude", 0.0)),
        Longitude=float(item.get("Longitude", 0.0)),
        AQI=int(item.get("AQI", -1)),
        Category_Name=item.get("Category", {}).get("Name", "Unknown")
    ) for item in data]
    
    df_airnow = spark.createDataFrame(processed_rows, schema)
    
    # Save to Bronze Delta Table
    # df_airnow.write.format("delta").mode("append").save("/mnt/data/bronze/weather")
    print("Weather data successfully fetched and staged.")
    df_airnow.show()
else:
    print("API Request Failed or returned empty.")