import joblib

from flask import Flask
from flask import request
from flask import jsonify

targets = ["updrs_1", "updrs_2", "updrs_3", "updrs_4"]
models = [joblib.load(f"./models/models_{u}.pkl") for u in targets]

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()['data'].split(',')

    results = {}
    for i, target in enumerate(targets):
        model = models[i]
        prediction = model.predict([[data[i]]])
        results[target] = float(prediction)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)