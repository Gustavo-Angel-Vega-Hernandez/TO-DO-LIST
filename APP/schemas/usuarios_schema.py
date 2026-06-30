from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateUser(BaseModel):
    nombre: str
    apellido_mat: str
    apellido_pat: str
    email: EmailStr
    contrasena_hash: str
    
class UpdateUser(BaseModel):
    nombre: Optional[str] = None
    apellido_mat: Optional[str] = None
    apellido_pat: Optional[str] = None
    email: Optional[EmailStr] = None
    """contrasena_hash: Optional[str] = None"""
    
class ShowUser(BaseModel):
    id_usuario: int
    nombre: str
    apellido_mat: str
    apellido_pat: str
    email: EmailStr
    
    class Config:
        from_attributes = True
        