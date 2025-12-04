from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import os
import time

import tensorflow as tf
from keras.models import load_model


app = Flask(__name__)

model_dir = os.path.join(os.path.dirname(__file__), "../backend/model")


model_path = os.path.join(model_dir, "crop_model_ann.h5")
model = load_model(model_path)

scaler_path = os.path.join(model_dir, "scaler.pkl")
scaler = pickle.load(open(scaler_path, "rb"))


encoder_path = os.path.join(model_dir, "label_encoder.pkl")
label_encoder = pickle.load(open(encoder_path, "rb"))


latest_sensor_data = {
    "N": 50, "P": 50, "K": 50,
    "temperature": 25.0, "humidity": 60,
    "ph": 6.5, "rainfall": 150.0
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/update-sensor-data", methods=["POST"])
def update_sensor_data():
    global latest_sensor_data
    try:
        data = request.json
        latest_sensor_data.update(data)
        return jsonify({"status": "success", "message": "Data updated"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/get-iot-data", methods=["GET"])
def get_iot_data():
    return jsonify(latest_sensor_data)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    

    features = np.array([[
        data["N"],
        data["P"],
        data["K"],
        data["temperature"],
        data["humidity"],
        data["ph"],
        data["rainfall"]
    ]])
    

    scaled_features = scaler.transform(features)
    
    time.sleep(0.5) 

    prediction_probs = model.predict(scaled_features)

    predicted_class_index = np.argmax(prediction_probs, axis=1)[0]

    recommended_crop = label_encoder.inverse_transform([predicted_class_index])[0]
    
    return jsonify({"recommended_crop": recommended_crop})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)