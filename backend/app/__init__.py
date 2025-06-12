from flask import Flask
from flask_cors import CORS  # Import CORS
from app.main import main  # Import your blueprint

def create_app():
    print("✅ Flask app is starting...") 
    app = Flask(__name__)
    
    CORS(app, origins=["http://localhost:3000"])  # Enable CORS here for the entire app

    app.register_blueprint(main)  # This makes /analyze available
    return app

