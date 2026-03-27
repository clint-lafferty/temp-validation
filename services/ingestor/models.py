from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class TempReading(db.Model):
    __tablename__ = 'temp_readings'
    
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    sensor_id = db.Column(db.String(50), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    
    def __init__(self, sensor_id, temperature, status):
        self.sensor_id = sensor_id
        self.temperature = temperature
        self.status = status