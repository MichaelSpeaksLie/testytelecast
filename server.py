from flask import Flask, request, jsonify, send_file
import csv
import os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Get the current directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the correct path for response.csv inside the same folder as index.html
CSV_FILE = os.path.join(BASE_DIR, "response.csv")

@app.route("/")
def home():
    return send_file(os.path.join(BASE_DIR, "index.html"))  # Serve the HTML file

@app.route("/submit", methods=["POST"])
def submit_comment():
    try:
        data = request.json
        name = data.get("name")
        roll = data.get("roll")
        feedback = data.get("feedback")
        message = data.get("message")

        if not all([name, roll, message]):
            return jsonify({"error": "Missing required fields"}), 400

        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date_str, time_str, name, roll, feedback, message])

        return jsonify({"message": "Your message has been received!"}), 200

    except Exception as e:
        print("Error:", str(e))  # Log error in terminal
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)

