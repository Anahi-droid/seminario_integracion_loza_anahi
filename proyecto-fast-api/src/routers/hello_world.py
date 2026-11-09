# app/routers/paso1_bienvenida.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv", 
            "autor": "Anahi Loza",
            "version": "0.1.0"}

@router.get("/anahi")
def endpoint_anahi() -> Mensaje:
    return Mensaje(texto="Hola", campo_interno = "Desde Anahi")

@router.get("/loza", response_model=Mensaje)
def endpoint_loza():
    return {"texto": "Hola", "prioridad": 5, "campo_interno": "no debería salir"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Anahi", 
            "prioridad": 2,
            "campo_interno": "Si deberia salir",
            "campo_extra": "No deberia salir"}