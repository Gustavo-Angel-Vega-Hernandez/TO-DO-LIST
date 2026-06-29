from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from APP.db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(VARCHAR(50), nullable=False)
    apellido_mat = Column(VARCHAR(30), nullable=False)
    apellido_pat = Column(VARCHAR(30), nullable=False)
    email = Column(VARCHAR(50), unique=True, nullable=False)
    contrasena_hash = Column(VARCHAR(255), nullable=False)
    
    
secciones = relationship("Seccion", back_populates="usuario")