def generar_planeacion_nem(datos):
    grado = datos.get("grado", "3° de Primaria")
    campo = datos.get("campo_formativo", "Lenguajes")
    metodologia = datos.get("metodologia", "Aprendizaje Basado en Proyectos")

    return {
        "datos_generales": {
            "nivel": "Primaria",
            "grado": grado,
            "campo_formativo": campo,
            "metodologia": metodologia
        },
        "vinculacion_nem": {
            "pda": [
                "Expresa ideas y emociones mediante textos orales y escritos",
                "Participa en intercambios comunicativos respetando turnos"
            ],
            "escenario": "Aula y comunidad",
            "enfoque": "Humanista, inclusivo y comunitario"
        },
        "secuencia_didactica": {
            "inicio": "Conversatorio sobre experiencias cotidianas del alumnado",
            "desarrollo": "Producción de textos breves en trabajo colaborativo",
            "cierre": "Lectura y reflexión colectiva sobre los textos producidos"
        },
        "evaluacion_formativa": {
            "estrategia": "Observación y retroalimentación continua",
            "instrumentos": ["Lista de cotejo", "Registro anecdótico"]
        }
    }
