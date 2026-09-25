
import re
import feedparser
from datetime import datetime
import os
import json

# Cargar feeds RSS desde archivo externo
with open("feeds_rss.json", "r", encoding="utf-8") as f:
    rss_feeds = json.load(f)

# Cargar palabras clave desde archivo externo
with open("keywords_ia.json", "r", encoding="utf-8") as f:
    keywords = json.load(f)

_patrones = [re.compile(r"\b" + re.escape(k.lower()) + r"\b") for k in keywords]

def contiene_palabra_clave(texto):
    texto = texto.lower()
    return any(p.search(texto) for p in _patrones)

def extraer_noticias():
    noticias_ai = []
    for fuente, url in rss_feeds.items():
        feed = feedparser.parse(url)
        for entrada in feed.entries:
            titulo = entrada.get("title", "")
            resumen = entrada.get("summary", "")
            contenido = f"{titulo} {resumen}".lower()
            if contiene_palabra_clave(contenido):
                noticia = {
                    "titulo": titulo,
                    "resumen": resumen,
                    "url": entrada.get("link", ""),
                    "publicado": entrada.get("published", ""),
                    "fuente": fuente
                }
                noticias_ai.append(noticia)

    if noticias_ai:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        log_dir = "log_history"
        os.makedirs(log_dir, exist_ok=True)
        path = os.path.join(log_dir, f"noticias_ia_{timestamp}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(noticias_ai, f, ensure_ascii=False, indent=2)
        print(f"📰 Noticias extraídas y guardadas: {path}")
        return noticias_ai
    else:
        print("⚠️ No se encontraron noticias relevantes.")
        return []
