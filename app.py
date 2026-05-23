from flask import Flask, render_template, request, jsonify, session
import json
import os

app = Flask(__name__)
app.secret_key = "mobileplace_secret_key_2024"

DATA_FILE = "sales_data.json"
USERS_FILE = "users_data.json"
BIN_FILE = "bin_data.json"

DEFAULT_USERS = {
    "admin": {"pass": "admin123", "role": "Admin", "name": "Admin"},
    "staff": {"pass": "staff123", "role": "Sales Staff", "name": "Staff"}
}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return DEFAULT_USERS

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def load_bin():
    if os.path.exists(BIN_FILE):
        with open(BIN_FILE, "r") as f:
            return json.load(f)
    return []

def save_bin(data):
    with open(BIN_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/login", methods=["POST"])
def login():
    users = load_users()
    body = request.json
    username = body.get("username", "").strip().lower()
    password = body.get("password", "")
    if username in users and users[username]["pass"] == password:
        session["user"] = {
            "username": username,
            "name": users[username]["name"],
            "role": users[username]["role"]
        }
        return jsonify({"success": True, "user": session["user"]})
    return jsonify({"success": False, "error": "Incorrect username or password."})

@app.route("/api/signup", methods=["POST"])
def signup():
    users = load_users()
    body = request.json
    fname = body.get("fname", "").strip()
    lname = body.get("lname", "").strip()
    username = body.get("username", "").strip().lower()
    password = body.get("password", "")
    role = body.get("role", "Sales Staff")
    if not fname or not lname or not username or not password:
        return jsonify({"success": False, "error": "Please fill in all fields."})
    if len(password) < 6:
        return jsonify({"success": False, "error": "Password must be at least 6 characters."})
    if username in users:
        return jsonify({"success": False, "error": "Username already exists."})
    users[username] = {"pass": password, "role": role, "name": fname + " " + lname}
    save_users(users)
    return jsonify({"success": True})

@app.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"success": True})

@app.route("/api/records", methods=["GET"])
def get_records():
    return jsonify(load_data())

@app.route("/api/records", methods=["POST"])
def add_record():
    data = load_data()
    record = request.json
    data.insert(0, record)
    save_data(data)
    return jsonify({"success": True})

@app.route("/api/records/bulk", methods=["PUT"])
def bulk_update_records():
    data = request.json
    save_data(data)
    return jsonify({"success": True})

@app.route("/api/records/<record_id>", methods=["PUT"])
def update_record(record_id):
    data = load_data()
    record = request.json
    for i, r in enumerate(data):
        if r.get("id") == record_id:
            data[i] = record
            break
    save_data(data)
    return jsonify({"success": True})

@app.route("/api/records/<record_id>", methods=["DELETE"])
def delete_record(record_id):
    data = load_data()
    data = [r for r in data if r.get("id") != record_id]
    save_data(data)
    return jsonify({"success": True})

@app.route("/api/bin", methods=["GET"])
def get_bin():
    return jsonify(load_bin())

@app.route("/api/bin", methods=["PUT"])
def update_bin():
    data = request.json
    save_bin(data)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
