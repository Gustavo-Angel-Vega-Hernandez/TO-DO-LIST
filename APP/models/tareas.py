from sqlalchemy import Column, Integer, VARCHAR, Date, ForeignKey
from sqlalchemy.orm import relationship
from APP.db.database import Base

class Tarea(Base):
    __tablename__ = "tareas"
    
    id_tarea = Column(Integer, primary_key= True)
    id_secciones = Column(Integer, ForeignKey("secciones.id_secciones"), nullable=False )
    titulo = Column(VARCHAR(30), nullable=False)
    descripcion = Column(VARCHAR(250), nullable=False)
    status = Column(VARCHAR(10))
    fecha_limite = Column(Date)
    

seccion = relationship("Seccion", back_populates="tareas")