
from modules.scraper import extraer_noticias
from modules.generador import generar_resumenes
from modules.exportador import subir_a_sheets

def main():
    noticias = extraer_noticias()
    if not noticias:
        return
    posts, consumo = generar_resumenes(noticias)
    subir_a_sheets(posts)
    print(f"✅ {len(posts)} publicaciones generadas.")
    print(f"💸 Tokens usados: {consumo['total_tokens']} | Coste aprox: ${consumo['usd']:.4f} / €{consumo['eur']:.4f}")

if __name__ == "__main__":
    main()
