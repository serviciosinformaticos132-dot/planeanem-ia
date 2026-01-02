from services.ia_generator import generar_planeacion_con_ia

@app.post("/planeacion/ia")
def planeacion_ia(datos: dict):
    return generar_planeacion_con_ia(datos)
