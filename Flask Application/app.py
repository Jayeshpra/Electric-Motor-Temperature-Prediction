import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load("Model Building\decision_tree_model.save")
trans = joblib.load("Model Building\mm_scaler.save")

app = Flask(__name__)

@app.route('/')
def predict():
    return render_template('Manual_prediict.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    x_test = [[float(x) for x in request.form.values()]]
    print('actual', x_test)
    x_test = trans.transform(x_test)
    print('transformed', x_test)
    pred = model.predict(x_test)

    return render_template('Manual_predict.html', prediction_text=('Permanent Magnet surface temperature: ', pred[0]))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)