from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["env_data"]
collection = db["temperature_readings"]

def store_temperature(data):
    collection.insert_one(data)
    print("Stored in MongoDB:", data)
