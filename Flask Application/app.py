import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load("Model Building\decision_tree_model.save")
x_trans = joblib.load("Model Building\mm_x_scaler.save")
y_trans = joblib.load("Model Building\mm_y_scaler.save")

app = Flask(__name__)

@app.route('/')
def predict():
    return render_template('Manual_predict.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    x_test = [[float(x) for x in request.form.values()]]
    # print('actual', x_test)
    x_test = x_trans.transform(x_test)
    # print('transformed', x_test)
    pred_scaled = model.predict(x_test)
    # print(pred_scaled)
    pred_scaled_2d = np.array(pred_scaled).reshape(-1, 1)
    # print(pred_scaled_2d)
    pred_celsius = y_trans.inverse_transform(pred_scaled_2d)
    # print(pred_celsius)
    pred_celsius_value = float(pred_celsius[0][0])
    # print(pred_celsius_value)

    return render_template('result.html', prediction_text=('Permanent Magnet surface temperature: ', pred_celsius_value))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)