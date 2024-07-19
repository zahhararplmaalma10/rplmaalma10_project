from flask import Flask, jsonify, request
from model import model
import pandas as pd

app = Flask(__name__)

sensorValues = {
    "distance": 0.0,
    "distance_per_step": 0.0,
    "coll_detected": False,
    "step": 0,
}

@app.route("/sensor", methods=["POST"])
def sensor_post_data():
    global sensorValues
    data = request.json
    previousDistance = sensorValues["distance"]
    distance = data.get('distance_cm', 0.0)
    sensorValues["distance"] = distance
    if distance <= 100 and not sensorValues["coll_detected"]:
        sensorValues["coll_detected"] = True
        sensorValues["distance_per_step"] = abs(previousDistance - distance)
        if sensorValues["step"] == 0:
            X = pd.DataFrame({
                "Jarak (cm)": [sensorValues["distance"]],
                "Jarak Langkah (cm)": [sensorValues["distance_per_step"]]
            })
            sensorValues["step"] = round(model.predict(X)[0])
    elif sensorValues["coll_detected"]:
        sensorValues["coll_detected"] = False
        sensorValues["distance_per_step"] = 0
        sensorValues["step"] = 0
    return jsonify(sensorValues)

@app.route("/sensor", methods=["GET"])
def sensor_get_data():
    global sensorValues
    return jsonify(sensorValues)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)