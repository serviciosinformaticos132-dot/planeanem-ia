from fastapi import FastAPI

app = FastAPI(
    title="PlaneaNEM IA",
    description="API para generar planeaciones NEM",
    version="0.1"
)

@app.get("/")
def inicio():
    return {
        "mensaje": "PlaneaNEM IA activo",
        "estado": "desarrollo"
    }

