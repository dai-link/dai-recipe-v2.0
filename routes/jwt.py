from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "ljhsdlknhdlkjskjhjkjsdhlkshdljhskdhkshdkljhsi87d89shdbsugdxiusbdigsdiu"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM, expiresIn=ACCESS_TOKEN_EXPIRE_MINUTES)
    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload:
            return payload.id
        else:
            return {
                "detail": "Invalid JWT Token",
                "status_code": 401
            }
    except JWTError:
        return None