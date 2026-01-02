def generar_planeacion_nem(grado, campo, metodologia):
    planeacion = {
        "grado": grado,
        "campo_formativo": campo,
        "metodologia": metodologia,
        "elementos_nem": {
            "PDA": [
                "Interpreta textos orales y escritos",
                "Expresa ideas de forma colaborativa"
            ],
            "escenario": "Aula y comunidad",
            "enfoque": "Humanista y comunitario"
        },
        "secuencia_didactica": {
            "inicio": "Conversatorio sobre experiencias previas",
            "desarrollo": "Actividad colaborativa con material contextual",
            "cierre": "Reflexión grupal y socialización"
        },
        "evaluacion": {
            "tipo": "Formativa",
            "instrumento": "Lista de cotejo y observación"
        }
    }

    return planeacion
