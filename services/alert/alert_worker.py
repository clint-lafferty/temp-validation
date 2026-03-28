import os
import time
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/temp_db')
def check_for_alerts():
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM temp_readings WHERE status IN ('critical', 'low')"))
        alerts = result.fetchall()
        for alert in alerts:
            print(f"ALERT: Sensor {alert['sensor_id']} reported {alert['temperature']}°C at {alert['timestamp']} with status {alert['status']}")