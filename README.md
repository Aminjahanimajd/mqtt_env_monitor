# IoT Environmental Monitoring System

## Overview

This project implements an integrated system to collect, process, and store real-time sensor data using MQTT, Python, and multiple database platforms (PostgreSQL, MongoDB, Neo4j). It demonstrates managing IoT big data efficiently across SQL, document, and graph databases.

## Features

- MQTT broker using Eclipse Mosquitto for sensor data ingestion.
- Python application to subscribe to MQTT topics and process data.
- Data storage:
  - Temperature sensor data in PostgreSQL (SQL).
  - Network device data in Neo4j (Graph).
  - Sensor raw data in MongoDB (Document).
- Docker Compose setup for easy multi-container orchestration.

## Technologies Used

- Python 3.13
- Paho MQTT client
- PostgreSQL + psycopg2
- MongoDB + pymongo
- Neo4j + py2neo
- Docker & Docker Compose
- Eclipse Mosquitto MQTT broker

## Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Aminjahanimajd/mqtt_env_monitor.git
   cd mqtt_env_monitor
