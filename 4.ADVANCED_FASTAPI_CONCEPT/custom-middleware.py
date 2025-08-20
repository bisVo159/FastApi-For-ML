import time 
from fastapi import FastAPI,Request
from starlette.middleware.base import BaseHTTPMiddleware

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request,call_next):
        start_time=time.time()
        print(f"Request: {request.method} {request.url}")

        response=await call_next(request)

        process_time=time.time()-start_time

        response.headers["X-Process-Time"] = str(round(process_time, 4))
        
        print(f"⬅️ Response status: {response.status_code} | Took {process_time:.4f}s")
        
        return response


app=FastAPI()

app.add_middleware(TimerMiddleware)

@app.get("/hello")
def read_root():
    for _ in range(10000):
        pass
    return {"message": "Welcome to the FastAPI application!"}
