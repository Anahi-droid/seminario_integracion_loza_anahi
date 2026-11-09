from fastapi import FastAPI
from routers.hello_world import router 

app = FastAPI(title="Curso FastAPI + uv")

app.include_router(router)