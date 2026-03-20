import sklearn

def load_data():
    return sklearn.datasets.load_iris(return_X_y=True)


def train_model(X, y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def save_model(model, filename="model.pkl"):
    import joblib
    joblib.dump(model, filename)


if __name__ == "__main__":
    modelx = train_model(*load_data())
    save_model(modelx)