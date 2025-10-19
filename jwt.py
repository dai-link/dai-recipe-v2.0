from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "ljhsdlknhdlkjskjhjkjsdhlkshdljhskdhkshdkljhsi87d89shdbsugdxiusbdigsdiu"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str = Depends(oauth2_schema)):
    

    credentials_exception = HTTPException(
        status_code = 401,
        detail = "Invalid or expired token",
        headers = {"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")

        if user_id is None:
            raise credentials_exception
        return user_id
    except JWTError:
        raise credentials_exception