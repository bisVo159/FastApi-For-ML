from fastapi import FastAPI, Depends

app=FastAPI()

class Settings:

    def __init__(self):
        print('init')
        self.api_key='key_secret'
        self.Debug=True

def get_settings():
    return Settings()

# both same

# @app.get("/config")
# def get_config(settings: Settings=Depends(get_settings)):
#     return {'api_key':settings.api_key,'Debug':settings.Debug}

@app.get("/config")
def get_config(settings:Settings=Depends(Settings)):
    return settings