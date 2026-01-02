from fastapi import FastAPI
from services.nem_engine import generar_planeacion_nem

app = FastAPI(
    title="PlaneaNEM IA",
    description="API para planeaciones NEM",
    version="0.2"
)

@app.get("/")
def inicio():
    return {"mensaje": "PlaneaNEM IA activo"}

@app.post("/planeacion/nem")
def crear_planeacion(datos: dict):
    return generar_planeacion_nem(datos)
