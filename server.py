from flask import Flask, request, jsonify
import csv
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

CSV_FILE = "response.csv"

# Ensure CSV file has headers
with open(CSV_FILE, "a", newline="") as file:
    writer = csv.writer(file)
    if file.tell() == 0:  # If file is empty, write headers
        writer.writerow(["Date", "Time", "Name", "Roll No", "Feedback", "Message"])

@app.route("/submit", methods=["POST"])
def submit_comment():
    data = request.json
    name = data.get("name")
    roll = data.get("roll")
    feedback = data.get("feedback")
    message = data.get("message")

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_str, time_str, name, roll, feedback, message])

    return jsonify({"message": "Your message has been received!"})

if __name__ == "__main__":
    app.run(debug=True)
