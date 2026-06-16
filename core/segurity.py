from jose import JWTError, jwt
from datetime import datetime, timedelta
# pyrefly: ignore [missing-import]
from passlib.context import CryptContext

# Configuración básica (puedes reemplazarlo por variables de entorno/settings si prefieres)
SECRET_KEY = "clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crear_token(sub: str, es_admin: bool):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {
        "sub": sub,
        "exp": expire,
        "es_admin": es_admin
    }
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)