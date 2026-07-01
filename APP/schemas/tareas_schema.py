from pydantic import BaseModel
from typing import Optional
from datetime import date

class CreateTarea (BaseModel):
    id_secciones: int
    titulo: str
    descripcion: str
    status: Optional[str] = "Pendiente"
    fecha_limite: Optional[date] = None
    
class UpdateTarea (BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    status: Optional[str] = None
    fecha_limite: Optional[date] = None
    
class ShowTarea (BaseModel):
    id_tarea: int
    id_secciones: int
    titulo: str
    descripcion: str
    status: str
    fecha_limite: Optional[date] = None
    
    class Config:
        from_attributes = True