from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Set up the MongoDB client
client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017/"))

# Connect to the database named 'flask_db'
db = client.flask_db

# Connect to the collection named 'data'
collection = db.data


# Define the route for the root URL
@app.route('/')
def index():
    # Return a welcome message with the current time
    return f"Welcome to the Flask app! The current time is: {datetime.now()}"


# Define the route for the '/data' endpoint
@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # Get JSON data from request
        data = request.get_json()

        # Insert data into MongoDB
        collection.insert_one(data)

        return jsonify({"status": "Data inserted"}), 201

    elif request.method == 'GET':
        # Fetch all documents except _id
        data = list(collection.find({}, {"_id": 0}))

        return jsonify(data), 200


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
