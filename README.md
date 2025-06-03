# 🧠 COOLSCRAPER – Automatización de noticias sobre Inteligencia Artificial

COOLSCRAPER es un sistema automatizado que recopila noticias relevantes sobre Inteligencia Artificial desde múltiples medios internacionales, genera resúmenes adaptados para redes sociales con ayuda de OpenAI y los exporta automáticamente a Google Sheets para su posterior publicación mediante plataformas como Make, Zapier o Buffer.

---

## ⚙️ Tecnologías utilizadas

- **Python 3.11+**
- **Feedparser** – Lectura de RSS/Atom Feeds
- **OpenAI API** – Generación de resúmenes con GPT
- **python-dotenv** – Gestión segura de claves
- **gspread** – Interacción con Google Sheets
- **oauth2client** – Autenticación con cuentas de servicio
- **schedule** – (opcional) Automatización horaria

---

## 📁 Estructura del proyecto

```
COOLSCRAPER/
├── inteligenciaartificial.py       # Scraper de noticias desde RSS
├── generador_post_ai.py            # Generador de títulos y resúmenes vía GPT
├── subir_a_sheets.py               # Exportador de resultados a Google Sheets
├── programador_ai.py               # (Opcional) Ejecución automatizada con schedule
├── .env                            # Variables de entorno (API KEY OpenAI)
├── google_service_account.json     # Credenciales Google API (no subir)
├── log_history/                    # Almacenamiento de resultados históricos
│   ├── noticias_ia_*.json
│   ├── posts_generados_*.json
│   └── token_usage_history.csv
├── README.md
└── .gitignore
```

---

## 🚀 Requisitos de instalación

1. Python 3.11 o superior (recomendado: [https://www.python.org](https://www.python.org))
2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## 📦 Contenido de `requirements.txt`

```text
feedparser
openai
python-dotenv
gspread
oauth2client
schedule
```

---

## 🔐 Configuración

### `.env`
Debes crear un archivo `.env` con tu clave de OpenAI:

```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### `google_service_account.json`
Genera un archivo de credenciales desde Google Cloud y compártelo con tu Google Sheet. Más detalles en `subir_a_sheets.py`.

---

## 🧪 Ejecución manual

```bash
py inteligenciaartificial.py         # Extrae noticias recientes
py generador_post_ai.py              # Genera resúmenes adaptados para redes
py subir_a_sheets.py                 # Exporta publicaciones a Google Sheets
```

---

## 🕒 Automatización (opcional)

Puedes usar `programador_ai.py` para lanzar todo el proceso automáticamente 3 veces al día utilizando la librería `schedule`.

---

## 📤 Integración con redes sociales

Una vez que los datos estén en Google Sheets, puedes conectar la hoja con herramientas como:

- [Make (Integromat)](https://www.make.com/)
- [Zapier](https://zapier.com/)
- [Buffer](https://buffer.com/)
- [n8n](https://n8n.io/)

---

## 🛡️ Seguridad

No subas los siguientes archivos a Git:

- `.env` – contiene tu API Key
- `google_service_account.json` – contiene tu acceso a Google Sheets

---

## 🧑‍💻 Autor

Desarrollado por William con asesoramiento de ChatGPT.  
Uso personal y profesional para automatizar tareas de contenido AI.
