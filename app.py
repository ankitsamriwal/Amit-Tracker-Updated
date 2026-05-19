from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json, os, config
from data_loader import load_dashboard_data

# template_folder='.' means Flask looks for HTML in the same folder as app.py
app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))
app.secret_key = config.SECRET_KEY
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"]   = True

_cache = {}

def get_data(force=False):
    if force or "data" not in _cache:
        _cache["data"] = load_dashboard_data(config.DATA_FOLDER, config.TRACKER_FILES)
    return _cache["data"]

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
    error = ""
    if request.method == "POST":
        u = request.form.get("username","")
        p = request.form.get("password","")
        if config.USERS.get(u) == p:
            session["user"] = u
            return redirect(url_for("dashboard"))
        error = "Invalid username or password."
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    data = get_data()
    return render_template("dashboard.html", data=json.dumps(data), user=session["user"])

@app.route("/api/refresh", methods=["POST"])
def api_refresh():
    if "user" not in session:
        return jsonify({"error": "Not logged in"}), 401
    data = get_data(force=True)
    return jsonify({"last_updated": data["last_updated"], "errors": data["errors"]})

@app.route("/api/data")
def api_data():
    if "user" not in session:
        return jsonify({"error": "Not logged in"}), 401
    return jsonify(get_data())

if __name__ == "__main__":
    get_data()
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
