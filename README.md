# 🎵 Bot Musiquero (YouTube to MP3 Automático)

Un script automatizado en Python diseñado para descargar canciones y playlists enteras desde YouTube u otras plataformas, convirtiéndolas directamente a formato MP3 de alta calidad. 

Simplemente le proporcionas una lista de títulos o enlaces (URLs), y el bot se encarga del resto mágicamente.

## ✨ Características Principales
- 🧠 **Búsqueda Inteligente:** Si solo sabes el nombre de la canción, el bot busca en YouTube y filtra inteligentemente los resultados para obtener la versión de "Sólo Audio" o "Lyrics", evitando introducciones largas de videos musicales.
- 🔗 **Soporte de URLs y Playlists:** Puedes pegar enlaces directos de videos, ¡e incluso enlaces de Playlists completas! El bot detectará si es una lista y descargará todos sus elementos a tu disco duro.
- ⚙️ **Autoinstalable:** No necesitas pelear con instalaciones. Si alguien sin la librería `yt-dlp` ejecuta el script, este se encargará de instalar sus propias dependencias por sí solo.
- 📁 **Organizado:** Crea una carpeta `/Descargas` donde organiza automáticamente todos los `.mp3` finalizados.

## 🚀 Cómo usarlo

### 1. Prerrequisitos
Lo único que necesitas para correr este programa es tener **[Python 3](https://www.python.org/downloads/)** instalado en tu computadora, y asegurarte de tener [FFmpeg](https://ffmpeg.org/download.html) disponible en tu sistema, el cual es el encargado de procesar y convertir el audio.

### 2. Configura tu lista
Abre el archivo `canciones.txt` (o créalo si no existe) y escribe una canción/enlace por línea:
```text
Queen - Bohemian Rhapsody
https://www.youtube.com/watch?v=dQw4w9WgXcQ
Eminem - Without Me
https://www.youtube.com/playlist?list=PLej... 
```

### 3. ¡Ejecútalo!
**Si estás en Windows:**
Haz doble clic en `iniciar.bat`.

**Si estás usando consola o Linux/Mac:**
Ejecuta el siguiente comando en tu terminal:
```bash
python descargador.py
```

---
*Hecho para evitar tareas repetitivas y disfrutar la música al instante. No promueve la piratería.*
