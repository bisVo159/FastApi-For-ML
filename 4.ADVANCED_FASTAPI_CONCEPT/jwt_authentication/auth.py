from datetime import datetime,timedelta,timezone
from authlib.jose import JoseError, jwt
from fastapi import HTTPException

SECRET_KEY="anikSecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    header= {'alg': ALGORITHM}
    expire= datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload=data.copy()
    payload.update({'exp':expire})
    print(payload)
    return jwt.encode(header,payload,SECRET_KEY)

def decode_token(token: str):
    try:
        claims=jwt.decode(token,key=SECRET_KEY)
        claims.validate()
        username=claims.get('sub')
        if username is None:
            raise HTTPException(status_code=401,detail="Could not validate credentials")
        return username
    except JoseError:
        raise HTTPException(status_code=401,detail="Could not validate credentials")
