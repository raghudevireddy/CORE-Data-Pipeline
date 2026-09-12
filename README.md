# C.O.R.E. (Continuous Oxygen Recovery Engine) 🌍 ♻️ 🏥

**Tech for Good: Purifying the air we breathe, one city at a time, while delivering life-saving oxygen to hospitals.**

## 📖 Project Overview
C.O.R.E. is an intelligent, real-time IoT fleet management and data pipeline built on **Databricks**. It manages a fleet of specialized eco-vehicles designed to extract CO2 and pollutants from the atmosphere, convert/purify it, and store the resulting Oxygen (O2). 

The C.O.R.E. system acts as the "brain" of the operation. It ingests live weather and air quality data to route empty vehicles to highly polluted areas, and ingests live hospital requests to dispatch full vehicles to medical centers in need of O2. 

*This project is non-profit and open-source, built to demonstrate the power of real-time Data Engineering in solving critical environmental and healthcare challenges.*

## 🏗️ Architecture (Medallion Data Pipeline)
This project utilizes a Databricks Lakehouse architecture processing streaming IoT data:
*   **Bronze Layer:** Ingests raw JSON telemetry from the fleet (GPS, O2 tank levels), weather API polling (AQI heatmaps), and hospital app requests.
*   **Silver Layer:** Cleanses coordinates, filters offline vehicles, and structures the data for real-time joins.
*   **Gold Layer (The Optimization Engine):** Merges fleet status, pollution zones, and hospital queues to calculate dynamic routing assignments.

## 🚀 Getting Started
To test the core logic of the pipeline locally, you can run the `core_simulator.py` script. It uses PySpark to simulate the data flows and routing decisions.
