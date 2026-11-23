from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

empleados_router = APIRouter()


class EmpleadoCreate(BaseModel):
    """Lo que el cliente envía para registrar un empleado. Sin id: lo asigna el servidor."""
    nombre: str = Field(min_length=3, max_length=100)
    cargo: str | None = None
    nivel: str = "junior"
    habilidades: list[str] = Field(default_factory=list)


class EmpleadoRead(BaseModel):
    """Lo que el servidor expone al leer un empleado. Incluye campos calculados por el servidor."""
    id: int
    nombre: str
    cargo: str | None
    nivel: str
    habilidades: list[str]
    activo: bool


class EmpleadoUpdate(BaseModel):
    """Lo que el cliente envía para actualizar. TODOS los campos son opcionales."""
    nombre: str | None = Field(default=None, min_length=3, max_length=100)
    cargo: str | None = None
    nivel: str | None = None
    habilidades: list[str] | None = None
    activo: bool | None = None


EMPLEADOS: list[dict] = [
    {
        "id": 1,
        "nombre": "María Torres",
        "cargo": "Analista de nómina",
        "nivel": "semisenior",
        "habilidades": [],
        "activo": True,
    },
    {
        "id": 2,
        "nombre": "Carlos Pérez",
        "cargo": "Reclutador",
        "nivel": "senior",
        "habilidades": [],
        "activo": True,
    },
]
NEXT_ID = 3


@empleados_router.post("/empleados", response_model=EmpleadoRead, status_code=201)
def crear_empleado(empleado: EmpleadoCreate) -> dict:
    global NEXT_ID
    nuevo = {
        "id": NEXT_ID,
        "activo": True,
        "notas_internas": "registrado desde la API",  # response_model lo filtra
        **empleado.model_dump(),
    }
    EMPLEADOS.append(nuevo)
    NEXT_ID += 1
    return nuevo


@empleados_router.get("/empleados", response_model=list[EmpleadoRead])
def listar_empleados() -> list[dict]:
    return EMPLEADOS


@empleados_router.patch("/empleados/{empleado_id}", response_model=EmpleadoRead)
def actualizar_empleado(empleado_id: int, cambios: EmpleadoUpdate) -> dict:
    for empleado in EMPLEADOS:
        if empleado["id"] == empleado_id:
            datos = cambios.model_dump(exclude_unset=True)
            empleado.update(datos)
            return empleado
    raise HTTPException(status_code=404, detail="Empleado no encontrado")


@empleados_router.post("/empleados/from-model")
def crear_desde_modelo(empleado: EmpleadoCreate) -> dict:
    # model_dump(): instancia de Pydantic -> dict plano de Python
    datos = empleado.model_dump()
    nuevo = {"id": len(EMPLEADOS) + 1, "activo": True, **datos}
    EMPLEADOS.append(nuevo)

    # model_validate(): dict de Python -> instancia validada de Pydantic
    validado = EmpleadoRead.model_validate(nuevo)
    return validado.model_dump()


@empleados_router.get("/empleados/{empleado_id}/raw-vs-validated")
def comparar_raw_validado(empleado_id: int) -> dict:
    raw = next((e for e in EMPLEADOS if e["id"] == empleado_id), None)
    if raw is None:
        return {"error": "no encontrado"}

    # model_validate lanza una excepción si el dict no cumple el schema de EmpleadoRead
    validado = EmpleadoRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validado.model_dump(),
        "validated_model_dump_json": validado.model_dump_json(),
    }


@empleados_router.delete("/empleados/{empleado_id}")
def eliminar_empleado(empleado_id: int) -> dict:
    for index, empleado in enumerate(EMPLEADOS):
        if empleado["id"] == empleado_id:
            eliminado = EMPLEADOS.pop(index)
            return {
                "message": "Empleado eliminado correctamente",
                "deleted_empleado": eliminado,
            }

    raise HTTPException(status_code=404, detail="Empleado no encontrado")


@empleados_router.get("/empleados/{empleado_id}", response_model=EmpleadoRead)
def obtener_empleado_por_id(empleado_id: int) -> dict:
    for empleado in EMPLEADOS:
        if empleado["id"] == empleado_id:
            return empleado

    raise HTTPException(status_code=404, detail="Empleado no encontrado")