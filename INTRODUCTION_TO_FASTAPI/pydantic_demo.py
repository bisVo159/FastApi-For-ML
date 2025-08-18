from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str = "Guest"

@app.get("/user/{user_id}", response_model=User)
def get_user(user_id: int):
    return User(id=user_id, name="ANik Biswas")