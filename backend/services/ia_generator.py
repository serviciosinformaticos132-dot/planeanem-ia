from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_planeacion_con_ia(datos):
    prompt = f"""
    Actúa como un experto en la Nueva Escuela Mexicana.
    Genera una planeación didáctica para:

    Nivel: Primaria
    Grado: {datos.get('grado')}
    Campo formativo: {datos.get('campo_formativo')}
    Metodología: {datos.get('metodologia')}

    Incluye:
    - PDA
    - Escenario
    - Inicio, desarrollo y cierre
    - Evaluación formativa
    Usa lenguaje docente mexicano.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return {"planeacion": response.choices[0].message.content}
