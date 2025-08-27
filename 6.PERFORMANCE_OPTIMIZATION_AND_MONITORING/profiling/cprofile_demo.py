import cProfile
import os
import time
import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

PROFILE_DIR="profiles"
os.makedirs(PROFILE_DIR,exist_ok=True)

app=FastAPI()

@app.middleware("http")
async def profile_requests(request:Request,call_next):
    profiler=cProfile.Profile()
    profiler.enable()
    
    response=await call_next(request)
    
    profiler.disable()
    
    timestamp=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path=request.url.path.strip('/').replace('/','_') or "root"
    profile_filename=os.path.join(PROFILE_DIR,f"profile_{path}_{timestamp}.prof")
    
    profiler.dump_stats(profile_filename)
    
    print(f"Profile data saved to {profile_filename}")
    
    return response


@app.get("/")
async def root():
    return {"message":"Welcome to the cProfile Demo!"}

@app.get("/compute")
async def compute():
    time.sleep(1)
    result = sum((i * 2) for i in range(10000))
    return JSONResponse({'result': result})