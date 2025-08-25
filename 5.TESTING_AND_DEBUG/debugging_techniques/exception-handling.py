from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class InvalidInputException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(InvalidInputException)
async def invalid_input_exception_handler(request: Request, exc: InvalidInputException):
    return JSONResponse(
        status_code=400,
        content={"message": f"Invalid input: {exc.name}"},
    )

@app.get('/test-exception/{name}')
def test_exception(name: str):
    if not name.isalpha():
        raise InvalidInputException(name=name)
    return {"message": f"Hello, {name}!"}