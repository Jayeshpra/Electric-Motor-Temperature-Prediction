import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load("D:\Jayesh\Git\GitHub repos\Electric-Motor-Temperature-Prediction\Model Building\decision_tree_model.save")
x_trans = joblib.load("D:\Jayesh\Git\GitHub repos\Electric-Motor-Temperature-Prediction\Model Building\mm_scaler_x.save")
y_trans = joblib.load("D:\Jayesh\Git\GitHub repos\Electric-Motor-Temperature-Prediction\Model Building\mm_scaler_y.save")

app = Flask(__name__)

@app.route('/')
def predict():
    return render_template('Manual_predict.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    x_test = [[float(x) for x in request.form.values()]]
    x_test = x_trans.transform(x_test)
    pred_scaled = model.predict(x_test)
    pred_scaled = np.array(pred_scaled).reshape(-1, 1) 
    pred_celsius = y_trans.inverse_transform(pred_scaled)
    pred_value = float(pred_celsius[0][0])
    result_text = f"Permanent Magnet surface temperature: {pred_value:.2f} °C"

    return render_template('result.html', prediction_text=result_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)