# C.O.R.E. (Continuous Oxygen Recovery Engine) 🌍 ♻️ 🏥

**Tech for Good: Purifying the air we breathe while delivering life-saving oxygen to hospitals.**

## 📖 Project Overview
C.O.R.E. is an intelligent, real-time IoT fleet management and data pipeline built on **Databricks**. It manages a fleet of eco-vehicles designed to extract CO2 from the atmosphere and store purified Oxygen (O2). 

The system acts as the fleet's "brain." It ingests live weather data (AirNow API) to route empty vehicles to highly polluted areas, and ingests live hospital requests to dispatch full vehicles to medical centers.

## 🏗️ Architecture (Medallion Data Pipeline)
*   **Bronze Layer:** Ingests raw JSON telemetry from the fleet (GPS, O2 levels), weather API polling, and hospital requests.
*   **Silver Layer:** Cleanses coordinates, filters offline vehicles, and structures the data for real-time joins.
*   **Gold Layer (Optimization Engine):** Prioritizes CRITICAL hospital requests; defaults to routing vehicles to the highest pollution zones.

## 📁 Repository Structure
* `/src/`: Contains the PySpark code for the Medallion pipeline.
  * `fetch_airnow_weather.py`: REST API polling.
  * `01_bronze_ingestion.py`: IoT Kafka streaming mockup.
  * `02_silver_cleansing.py`: Data standardization.
  * `03_gold_routing.py`: The routing algorithm.