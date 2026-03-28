import os
import time
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/temp_db')
engine = create_engine(DATABASE_URL)

def check_for_alerts():
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM temp_readings WHERE status IN ('critical', 'low')"))
        for alert in result.mappings():
            print(f"ALERT: Sensor {alert['sensor_id']} reported {alert['temperature']}°C at {alert['timestamp']} with status {alert['status']}")

if __name__ == "__main__":
    while True:
        try:
            check_for_alerts()
        except Exception as e:
            print(f"Error checking alerts: {e}")
        
        # Wait 10 seconds before checking again
        time.sleep(10)
