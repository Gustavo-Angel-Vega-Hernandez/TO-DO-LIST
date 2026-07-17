from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from APP.models.tareas import Tarea
from APP.schemas.tareas_schema import CreateTarea, UpdateTarea

#Operaciones

# 1. Crear una tarea
# 2. Obtener una tarea
# 3. Mostrar todas las tareas
# 4. Modificar una tarea
# 5 Eliminar una tarea
# 6. Cambiar status de la tarea
