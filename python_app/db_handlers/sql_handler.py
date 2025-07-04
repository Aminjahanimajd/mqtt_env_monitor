import psycopg2

conn = psycopg2.connect(
    dbname="envdb",
    user="postgres",
    password="admin",  # replace with your password
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS temperature_log (
    id SERIAL PRIMARY KEY,
    temperature FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def store_temperature_sql(temp):
    cursor.execute("INSERT INTO temperature_log (temperature) VALUES (%s)", (temp,))
    conn.commit()
    print("Stored in SQL:", temp)
