from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # If you want to use templates, put an index.html in main/templates/
    try:
        return render_template("index.html")
    except Exception:
        return "<h1>Flask Lab Project</h1><p>Welcome to the homepage.</p>", 200


@app.route("/health")
def health():
    return "OK", 200


@app.route("/data", methods=["POST"])
def data():
    """
    Accepts JSON or form data. Returns an echo of received data and a status.
    """
    if request.is_json:
        payload = request.get_json()
    else:
        # fall back to form values
        payload = request.form.to_dict()

    # Example validation
    if not payload:
        return jsonify({"error": "no data provided"}), 400

    return jsonify({"status": "received", "data": payload}), 201


if __name__ == "__main__":
    # For local dev only. In production use gunicorn or another WSGI server.
    app.run(host="0.0.0.0", port=5000, debug=True)
