from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import create_access_token, decode_token
from schemas import Token
from utils import get_user, verify_password

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = get_user(form_data.username)
    if not user_dict or not verify_password(form_data.password, user_dict['hashed_password']):
        raise HTTPException(400, detail='Invalid credentials')
    
    access_token = create_access_token(data={'sub': form_data.username})
    return Token(access_token=access_token,token_type='bearer')
    # return {'access_token': access_token, 'token_type': 'bearer'}


@app.get('/users')
def read_users(token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    return {'username': username}