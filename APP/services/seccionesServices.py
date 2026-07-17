from sqlalchemy.ext.asyncio import async_session
from sqlalchemy import select
from APP.models.secciones import Seccion
from APP.schemas.secciones_schema import createSection, UpdateSection

#Operaciones

# 1. Crear una seccion
# 2. Obtener una seccion
# 3. Mostrar todas las secciones
# 4. Modificar una seccion
# 5 Eliminar una seccion