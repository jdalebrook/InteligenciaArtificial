import os
from datetime import datetime

import gspread
from dotenv import load_dotenv

load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SERVICE_ACCOUNT_PATH = os.getenv("GOOGLE_SERVICE_ACCOUNT_PATH", "doc/google_service_account.json")
HEADER = ["fecha", "titulo_original", "url", "contenido_generado", "estado"]


def subir_a_sheets(posts):
    if not posts:
        return
    if not SPREADSHEET_ID or not os.path.exists(SERVICE_ACCOUNT_PATH):
        print("⚠️ Google Sheets no configurado (SPREADSHEET_ID / credenciales). Se omite la exportación.")
        return

    cliente = gspread.service_account(filename=SERVICE_ACCOUNT_PATH)
    hoja = cliente.open_by_key(SPREADSHEET_ID).sheet1
    if not hoja.row_values(1):
        hoja.append_row(HEADER)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    filas = [[fecha, p["titulo_original"], p["url"], p["contenido_generado"], "pendiente"] for p in posts]
    hoja.append_rows(filas, value_input_option="USER_ENTERED")
    print(f"📤 {len(filas)} filas exportadas a Google Sheets.")
