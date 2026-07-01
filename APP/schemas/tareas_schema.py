from pydantic import BaseModel
from typing import Optional
from datetime import date

class CreateTarea (BaseModel):
    id_secciones: int
    titulo: str
    descripcion: str
    status: str
    fecha_limite: date
    
class UpdateTarea (BaseModel):
    id_tarea: Optional[int] = None
    id_secciones: Optional[int] = None
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    status: Optional[str] = None
    fecha_limite: Optional[date] = None
    
class ShowTarea (BaseModel):
    id_tarea: Optional[int] = None
    id_secciones: Optional[int] = None
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    status: Optional[str] = None
    fecha_limite: Optional[date] = None
    
    class config:
        from_atributes: True