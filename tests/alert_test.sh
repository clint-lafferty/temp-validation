#!/bin/bash
curl -X POST http://localhost:5000/ingest \
     -H "Content-Type: application/json" \
     -d '{"sensor_id": "TEST_SENSOR_99", "temperature": 95.5}'

sleep 12

docker compose logs alert | grep "TEST_SENSOR_99"
