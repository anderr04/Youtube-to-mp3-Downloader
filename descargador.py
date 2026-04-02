import os
import sys

# Instalar yt-dlp automáticamente si no está instalado
try:
    import yt_dlp
except ImportError:
    print("yt-dlp no está instalado. Instalándolo automáticamente...")
    os.system(f'"{sys.executable}" -m pip install yt-dlp')
    import yt_dlp

def descargar_canciones(archivo_texto):
    if not os.path.exists(archivo_texto):
        print(f"❌ No se encontró el archivo '{archivo_texto}'.")
        print("Creando uno de ejemplo...")
        with open(archivo_texto, "w", encoding="utf-8") as f:
            f.write("Queen - Bohemian Rhapsody\n")
            f.write("Daft Punk - Get Lucky\n")
        print(f"¡Archivo '{archivo_texto}' creado! Agrégale el nombre de tus canciones y vuelve a ejecutar el programa.")
        return

    with open(archivo_texto, "r", encoding="utf-8") as f:
        # Filtrar líneas vacías
        canciones = [line.strip() for line in f if line.strip()]

    if not canciones:
        print(f"⚠️ El archivo {archivo_texto} está vacío. Añade el título de algunas canciones.")
        return

    print(f"🎵 Encontradas {len(canciones)} canciones o enlaces para descargar.")

    carpeta_salida = "Descargas"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Opciones de yt-dlp base para descargar formato mp3
    opciones_base = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320', # Máxima calidad posible en MP3
        }],
        'outtmpl': f'{carpeta_salida}/%(title)s.%(ext)s', # Guardar en la carpeta Descargas
        'quiet': False,
    }

    for i, cancion in enumerate(canciones, 1):
        es_url = cancion.startswith("http://") or cancion.startswith("https://")
        
        # Copiamos las opciones base para configurarlas según si es URL o búsqueda
        opciones = dict(opciones_base)
        
        if es_url:
            busqueda = cancion
            print(f"\n==================================================")
            print(f"[{i}/{len(canciones)}] Detectada URL: {cancion}")
            
            opciones['default_search'] = 'auto'
            # Permitimos descargar la playlist si es una URL que contiene 'list='
            if "list=" in cancion:
                opciones['noplaylist'] = False
                print(f"      (¡Se ha detectado una Playlist! Descargando todos los videos...)")
            else:
                opciones['noplaylist'] = True
            print(f"==================================================")
        else:
            busqueda = f"{cancion} lyrics"
            print(f"\n==================================================")
            print(f"[{i}/{len(canciones)}] Buscando: {cancion}")
            print(f"      (Término inteligente usado: '{busqueda}')")
            print(f"==================================================")
            
            opciones['default_search'] = 'ytsearch1'
            opciones['noplaylist'] = True

        # Inicializamos el descargador con las opciones de este turno
        with yt_dlp.YoutubeDL(opciones) as ydl:
            try:
                ydl.download([busqueda])
                print(f"✅ ¡Descarga completada!")
            except Exception as e:
                print(f"❌ Error al procesar '{cancion}': {e}")
                
    print("\n🎉 ¡Todas las descargas han finalizado!")

if __name__ == "__main__":
    descargar_canciones("canciones.txt")
    print("\nPresiona ENTER para cerrar el programa...")
    input()
