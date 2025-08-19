from fastapi import FastAPI
from schemas import InputSchema,OutputSchema
from predict import make_prediction,batch_prediction
from typing import List

app=FastAPI()

@app.get('/')
def index():
    return {'message': 'Welcome to the ML Model Prediction API'}

@app.post("/prediction",response_model=OutputSchema)
def predict(user_input:InputSchema):
    prediction=make_prediction(user_input.model_dump())
    return OutputSchema(predicted_price=round(prediction,2))

@app.post("/batch-prediction",response_model=List[OutputSchema])
def predict(user_input:List[InputSchema]):
    predictions=batch_prediction([x.model_dump() for x in user_input])
    return [OutputSchema(predicted_price=round(prediction,2)) for prediction in predictions]