from flask import Flask, request, jsonify
from models import db, TempReading
import os

def create_app():
    app = Flask(__name__)
    
    # Configure the database URI
    user = os.getenv('DB_USER', 'iot_user')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    name = os.getenv('DB_NAME')

    TEMP_CRITICAL = float(os.getenv('TEMP_THRESHOLD_CRITICAL'))
    TEMP_LOW = float(os.getenv('TEMP_THRESHOLD_LOW'))

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    from models import db
    db.init_app(app)
    
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    # Register blueprints or routes here if needed
    @app.route('/ingest', methods=['POST'])
    def ingest_data():
        data = request.json
        temp = data.get('temperature')

        status = 'normal'
        if temp >= TEMP_HIGH:
            status = 'critical'
        elif temp <= TEMP_LOW:
            status = 'low'
        
        new_reading = TempReading(
            sensor_id=data.get('sensor_id'),
            temperature=temp,
            status=status
        )
        db.session.add(new_reading)
        db.session.commit()

        return jsonify({'message': 'Data ingested successfully'}), 201


    return app
