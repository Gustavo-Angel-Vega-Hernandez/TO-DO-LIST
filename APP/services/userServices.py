from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from APP.models.usuarios import Usuario
from APP.schemas.usuarios_schema import CreateUser, UpdateUser
from APP.core.security import verificar_password

#Operaciones

# 1. Obtener un usuario (inicio de sesion)
async def obtner_usuario_por_email (db: AsyncSession, email_usuario: str) -> Usuario | None:
    stmt = select(Usuario).where(Usuario.email == email_usuario)
    resultado = await db.execute(stmt)
    return resultado.scalar_one_or_none

async def autenticar_usuario (db: AsyncSession, email_usuario: str, password_plano: str) -> Usuario | None:
    usuario = await obtner_usuario_por_email(db, email_usuario)
    
    if not usuario:
        return None
    
    password_es_correcta = verificar_password(password_plano, usuario.contrasena_hash)
    
    if not password_es_correcta:
        return None
    
    return usuario


# 2. Crear un usuaio
# 3. Modificar un usuario
# 4. Dar de baja un usuario