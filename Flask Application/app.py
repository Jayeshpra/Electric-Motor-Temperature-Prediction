import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("D:\\Jayesh\\Git\\GitHub repos\\Electric-Motor-Temperature-Prediction\\Model Building\\decision_tree_model.save")
x_trans = joblib.load("D:\\Jayesh\\Git\\GitHub repos\\Electric-Motor-Temperature-Prediction\\Model Building\\mm_scaler_x.save")
y_trans = joblib.load("D:\\Jayesh\\Git\\GitHub repos\\Electric-Motor-Temperature-Prediction\\Model Building\\mm_scaler_y.save")

app = Flask(__name__)

@app.route('/')
def predict():
    return render_template('Manual_predict.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    x_input = [[float(x) for x in request.form.values()]]
    x_data = pd.DataFrame(x_input)
    scaled_x = x_trans.transform(x_data)
    pred_value = model.predict(scaled_x)
    pred_df = pd.DataFrame(pred_value)
    scaled_y = y_trans.inverse_transform(pred_df)
    result_text = f"Permanent Magnet surface temperature: {scaled_y} °C"

    return render_template('result.html', prediction_text=scaled_y)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)