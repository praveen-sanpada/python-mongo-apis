# app.py
from flask import Flask, jsonify
from config import Config
from routes.venue_routes import venue_bp

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Register blueprint for venue routes
app.register_blueprint(venue_bp)

# Custom JSON encoder for MongoDB ObjectId serialization
from bson import ObjectId
import json

class MongoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)  # Convert ObjectId to string
        return super().default(obj)

# Set custom JSON encoder
app.json.encoder = MongoJSONEncoder

# Main entry point to run the app
if __name__ == "__main__":
    app.run(debug=True)
