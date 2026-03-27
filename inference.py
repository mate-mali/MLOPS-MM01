import joblib
from api.models.iris import PredictRequest, PredictResponse
from sklearn.datasets import load_iris


def load_model(filename="model.pkl"):
    return joblib.load(filename)

def predict_model(model, X: PredictRequest):
    ze_response = model.predict(X.to_numpy())
    ze_label = load_iris().target_names[ze_response][0]
    return ze_label


