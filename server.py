from flask import Flask, request, jsonify, render_template
import csv
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CSV_FILE = "response.csv"

@app.route("/")
def home():
    return open("index.html").read()

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
