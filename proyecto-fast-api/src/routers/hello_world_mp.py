from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EmpleadoPublico(BaseModel):
    nombre: str
    cargo: str
    prioridad: int = 1


class EmpleadoInterno(EmpleadoPublico):
    salario: int


@router.get("/")
def read_root() -> dict[str, str]:
    return {
        "mensaje": "Bienvenido al sistema de Recursos Humanos",
        "autor": "Anahi Loza",
        "version": "0.1.0",
    }


@router.get("/empleado", response_model=EmpleadoPublico)
def endpoint_empleado():
    return EmpleadoInterno(nombre="Juan", cargo="Analista", salario=900)


@router.get("/contratacion", response_model=EmpleadoPublico)
def endpoint_contratacion():
    return {"nombre": "Carla", "cargo": "Reclutadora", "prioridad": 5, "salario": 1200}


@router.get("/campo-extra", response_model=EmpleadoPublico)
def endpoint_campo_extra():
    return {
        "nombre": "Pedro",
        "cargo": "Asistente",
        "prioridad": 2,
        "salario": 800,
        "campo_extra": "departamento confidencial",
    }