import joblib

targets = ["updrs_1", "updrs_2", "updrs_3", "updrs_4"]

models = [joblib.load(f"./models/models_{u}.pkl") for u in targets]

def predict(data):

    results = {}
    for i, target in enumerate(targets):
        model = models[i]
        prediction = model.predict([[data[i]]])
        results[target] = float(prediction)

    return results

def lambda_handler(event, context):
    data = event['data']
    result = predict(data)
    return result
