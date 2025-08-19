import joblib
import numpy as np
from typing import List

saved_model = joblib.load('model.joblib')
print('Loaded the Model')


def make_prediction(data: dict) -> float:
    features = np.array([
        [
            data['longitude'],
            data['latitude'],
            data['housing_median_age'],
            data['total_rooms'],
            data['total_bedrooms'],
            data['population'],
            data['households'],
            data['median_income']
        ]
    ])
    return saved_model.predict(features)[0]

def batch_prediction(data: List[dict]):
    X = np.array([
        [
            d['longitude'],
            d['latitude'],
            d['housing_median_age'],
            d['total_rooms'],
            d['total_bedrooms'],
            d['population'],
            d['households'],
            d['median_income']
        ] for d in data
    ])
    return saved_model.predict(X)