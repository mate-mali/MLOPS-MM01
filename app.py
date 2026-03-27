from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
from inference import load_model,  predict_model
from training import load_data, train_model, save_model
app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/train")
def train_model_endpoint():
    model = train_model(*load_data())
    save_model(model)
    return {"message": "Model trained and saved successfully"}

# @app.post("/predict")
# def predict_endpoint(request: PredictRequest) -> PredictResponse:
#     model = load_model()
#     prediction = predict(model, request.model_dump())
#     return PredictResponse(prediction=prediction)

@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    model = load_model()
    print(request)
    prediction = predict_model(model, request)
    return PredictResponse(prediction=prediction) #this shoudl return name of the iris from iris.target_names and according to swagger testing it does 