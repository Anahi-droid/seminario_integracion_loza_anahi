from fastapi import FastAPI
from routers.hello_world_mp import router as hello_router
from routers.tasks_router_mp import empleados_router

app = FastAPI(title="Curso FastAPI + uv")

app.include_router(hello_router)
app.include_router(empleados_router)