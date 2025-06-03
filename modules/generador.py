
import os
import json
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generar_resumenes(noticias):
    resultados = []
    total_input_tokens = 0
    total_output_tokens = 0

    for i, noticia in enumerate(noticias):
        prompt = f"""
Crea un título atractivo y un resumen breve (máximo 280 caracteres) para redes sociales a partir de esta noticia sobre inteligencia artificial. Sé claro, directo e interesante. Agrega la URL al final del resumen.

Título original: {noticia['titulo']}
Resumen: {noticia['resumen']}
Fuente: {noticia['fuente']}
Publicado: {noticia['publicado']}
URL: {noticia['url']}
"""
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un redactor experto en publicaciones para redes sociales sobre tecnología e inteligencia artificial."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        content = respuesta.choices[0].message.content.strip()

        input_tokens = respuesta.usage.prompt_tokens
        output_tokens = respuesta.usage.completion_tokens
        total_input_tokens += input_tokens
        total_output_tokens += output_tokens

        resultados.append({
            "titulo_original": noticia["titulo"],
            "url": noticia["url"],
            "contenido_generado": content
        })

    total_tokens = total_input_tokens + total_output_tokens
    cost_usd = (total_input_tokens * 0.0005 + total_output_tokens * 0.0015) / 1000
    cost_eur = cost_usd * 0.93  # Aproximación actual

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    log_dir = r"C:\COOLSCRAPER\InteligenciaArtificial\log_history"
    os.makedirs(log_dir, exist_ok=True)
    path = os.path.join(log_dir, f"posts_generados_{timestamp}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    print(f"✍️ Resúmenes generados y guardados: {path}")
    return resultados, {
        "total_tokens": total_tokens,
        "input_tokens": total_input_tokens,
        "output_tokens": total_output_tokens,
        "usd": round(cost_usd, 4),
        "eur": round(cost_eur, 4)
    }
