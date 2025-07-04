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

   git clone https://github.com/Aminjahanimajd/mqtt_env_monitor.git
   cd mqtt_env_monitor

2. Ensure Docker and Docker Compose are installed and running.

3. Start services:
  docker-compose up -d

4. Install Python dependencies:
  pip install -r requirements.txt

5. Run the publisher and subscriber scripts:
  python python_app/mqtt_publisher.py
  python python_app/mqtt_subscriber.py

## Usage

The publisher simulates IoT sensor data publishing to MQTT topics.

The subscriber receives messages and stores data in appropriate databases.

Use database clients to inspect stored data.

## Project Structure

docker-compose.yml - Docker services configuration.

python_app/ - Python scripts and DB handler modules.

README.md - This documentation.

## Future Work

Develop a web dashboard for real-time data visualization.

Implement data analytics and alerts.

Expand sensor types and improve fault tolerance.

## Author
Amin Jahanimajd
Data Analysis Bachelor’s Student
University of Messina
