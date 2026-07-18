from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from APP.models.usuarios import Usuario
from APP.schemas.usuarios_schema import CreateUser, UpdateUser
from APP.core.security import verificar_password, obtener_password_hash

#Operaciones

# 1. Obtener un usuario (inicio de sesion)
async def obtner_usuario_por_email (db: AsyncSession, email_usuario: str) -> Usuario | None:
    stmt = select(Usuario).where(Usuario.email == email_usuario)
    resultado = await db.execute(stmt)
    return resultado.scalar_one_or_none()

async def autenticar_usuario (db: AsyncSession, email_usuario: str, password_plano: str) -> Usuario | None:
    usuario = await obtner_usuario_por_email(db, email_usuario)
    
    if not usuario:
        return None
    
    password_es_correcta = verificar_password(password_plano, usuario.contrasena_hash)
    
    if not password_es_correcta:
        return None
    
    return usuario

# 2. Crear un usuaio

async def crear_usuario (db: AsyncSession, usuario_in: CreateUser) -> Usuario:
    contraseña_hash_generada = obtener_password_hash(usuario_in.contrasena_hash)
    
    #Convertir el objeto pydantic en un diccionario de python 
    datos_del_usuario = usuario_in.model_dump()
    datos_del_usuario["contrasena_hash"] = contraseña_hash_generada
    
    #Se convierte el diccionario a un objeto de memoria que representa una fila de la tabla
    nuevo_usuario = Usuario(**datos_del_usuario)
    
    db.add(nuevo_usuario) #Se coloca el objeto en la salda de espera como en git
    await db.commit() #Envia los datos a la BD
    await db.refresh(nuevo_usuario) #Trae el objeto ahora desde la BD esto para actualizarlo (esto para traer los datos que genera la BD como el ID)
    
    return nuevo_usuario
    

# 3. Modificar un usuario
# 4. Dar de baja un usuario