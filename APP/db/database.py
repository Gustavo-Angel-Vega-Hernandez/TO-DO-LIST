#Alchemy es un ORM que basicamente es un traductor entre python y las BD
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
#La funcion create_async_engine es un motor asincrono que crea un pool de conexiones a la BD para que no sea lento
#La funcion async_sessionMaker crea multiples seciones configuradas y las limpia una vez las usas 
from APP.core.config import settings
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(settings.DATABASE_URL, echo=True); #Crea la conexion con los datos del .env

AsyncSessionLocal = async_sessionmaker(
    bind = engine, #Vinculas un motor (inyectar una seccion para hacer peticiones)
    autocommit=False, #Autoguardado desactivado
    autoflush=False, #Sincronización previa automática desactivada
    expire_on_commit=False #No expirar los datos de los objetos después de guardar
)

class Base(DeclarativeBase):
    pass
