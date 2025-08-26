import redis
import joblib
import hashlib
import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

model = joblib.load('model.joblib')

class IrisFlower(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    def to_list(self):
        return [
            self.SepalLengthCm,
            self.SepalWidthCm,
            self.PetalLengthCm,
            self.PetalWidthCm
        ]

    def generate_cache_key(self) -> str:
        data_string = json.dumps(self.model_dump(), sort_keys=True)
        return hashlib.sha256(data_string.encode()).hexdigest()
    
@app.post("/predict")
def predict(iris: IrisFlower):
    cache_key = iris.generate_cache_key()
    cached_result = redis_client.get(cache_key)
    
    if cached_result:
        print("Cache hit")
        return json.loads(cached_result)
    
    prediction = int(model.predict([iris.to_list()])[0])
    result = {'prediction': prediction}
    redis_client.set(cache_key, json.dumps(result))
    
    return result