import joblib
import json
def predict(data):

    #Load the data to run prediction on, model and pipeline
    jsondata = json.loads(json.dumps(data))
    print("---------------------------------")
    print(type(jsondata))
    print("---------------------------------")
    dt = []
    dt.append(jsondata['SepalLengthCm'])
    dt.append(jsondata['SepalWidthCm'])
    dt.append(jsondata['PetalLengthCm'])
    dt.append(jsondata['PetalWidthCm'])
    raw = [dt]

    #Load the data to run prediction on, model and pipeline
    model = joblib.load("irismodel.pkl")

    # Run prediction
    result = model.predict(raw)
    print(result)

    return {'prediction': result[0]}
