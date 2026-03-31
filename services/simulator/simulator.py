import requests
import time
import random
import os

INGEST_URL = os.getenv('INGESTOR_URL', 'http://ingestor:5000/ingest')

def simulate_temperature_readings():
    sensor_id = f'sensor_{random.randint(1, 10)}'
    while True:
        temperature = round(random.uniform(40, 80), 2)  # Simulate temperature between 40 and 80
        data = {
            'sensor_id': sensor_id,
            'temperature': temperature
        }
        try:
            response = requests.post(INGEST_URL, json=data)
            if response.status_code == 201:
                print(f'Sent data: {data}')
            else:
                print(f'Failed to send data: {response.text}')
        except Exception as e:
            print(f'Error sending data: {e}')
        
        time.sleep(5)  # Wait for 5 seconds before sending the next reading

if __name__ == '__main__':
    simulate_temperature_readings()