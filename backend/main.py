from fastapi import FastAPI
from services.nem_engine import generar_planeacion_nem

app = FastAPI(title="PlaneaNEM IA")

@app.get("/")
def inicio():
    return {"mensaje": "PlaneaNEM IA activo"}

@app.post("/generar")
def generar(datos: dict):
    return generar_planeacion_nem(
        grado=datos.get("grado", "3°"),
        campo=datos.get("campo", "Lenguajes"),
        metodologia=datos.get("metodologia", "ABP")
    )
