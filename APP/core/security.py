from passlib.context import CryptContext

#Se configura el motor de encriptacion (Hash) y se especifica el uso de bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_password (plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def obtner_password_hash(password: str) -> str:
    return pwd_context.hash(password)
