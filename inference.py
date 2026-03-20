import joblib

def load_model(filename="model.pkl"):
    return joblib.load(filename)

def predict(model, X):
    return model.predict(X)

