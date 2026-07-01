from pydantic import BaseModel
from typing import Optional

class createSection(BaseModel):
    id_usuario: int 
    nombreseccion: str
    
class UpdateSection(BaseModel):
    nombreseccion: Optional[str] = None
    
class ShowSection(BaseModel):
    id_secciones: int
    id_usuario: int
    nombreseccion: str
    
    class Config:
        from_attributes = True