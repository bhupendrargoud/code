import os
from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = int(os.getenv("PORT", 8000))
MSG = os.getenv("MSG", "api response")

@app.route("/headers", methods=["GET"])
def get_headers():
    return jsonify({"headers": dict(request.headers)})

@app.route("/ip", methods=["GET"])
def get_client_ip():
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return jsonify({"client_ip": client_ip})

@app.route("/", defaults={"full_path": ""}, methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
@app.route("/<path:full_path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
def catch_all(full_path):
    return jsonify({
        "message": MSG
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)

