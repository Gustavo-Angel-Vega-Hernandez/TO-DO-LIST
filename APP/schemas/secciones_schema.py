from pydantic import BaseModel
from typing import Optional

class createSection(BaseModel):
    id_usuario: int 
    nombreseccion: str
    
class UpdateSection(BaseModel):
    id_seccion: Optional[int] = None
    id_usuario: Optional[int] = None
    nombreseccion: Optional[str] = None
    
class ShowSection(BaseModel):
    id_seccion: int
    id_usuario: int
    nombreseccion: str
    
    class config:
        from_atributes: True