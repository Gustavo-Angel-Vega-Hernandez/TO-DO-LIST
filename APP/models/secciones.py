from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from APP.db.database import Base

class Seccion (Base):
    __tablename__ = "secciones"
    
    id_secciones = Column(Integer, primary_key=True)
    id_usuario = Column(Integer,  ForeignKey("usuarios.id_usuario"), nullable= False)
    nombreseccion = Column(VARCHAR(30), nullable=False)
    

usuario = relationship("Usuario", back_populates="secciones")
tareas = relationship("Tarea", back_populates="seccion")