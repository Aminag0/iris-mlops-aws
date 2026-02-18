from flask import Flask, request, jsonify
import joblib
import numpy as np
import redis
import os
import json

app = Flask(__name__)

model = joblib.load("model.pkl")

redis_host = os.environ.get("REDIS_HOST", "redis")
cache = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    return "ML Model with Redis Cache is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data["features"]
    key = json.dumps(features)

    if cache.exists(key):
        return jsonify({"prediction": int(cache.get(key)), "cached": True})

    features_np = np.array(features).reshape(1, -1)
    prediction = model.predict(features_np)[0]

    cache.set(key, int(prediction))

    return jsonify({"prediction": int(prediction), "cached": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
