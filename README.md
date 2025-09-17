# 📸 Organizador de Fotos

Autor: Santiago Camilo Rey Benavides  
Pontificia Universidad Javeriana – Ingeniería de Sistemas

---

## Descripción General

Programa en **Python** que organiza automáticamente fotos y videos por la **fecha en que fueron tomados**.  
El script:

- Escanea una carpeta de origen (memoria de cámara, disco, etc.)
- Copia los archivos a un directorio de destino
- Crea subcarpetas por **día de captura**
- Genera **miniaturas (thumbnails)** de altura máxima de 100 píxeles

---

## Uso desde línea de comandos

```bash
./organizador_de_fotos.py -s path/de/la/fuente -d path/del/destino
```

Parámetros:

- **-s** : Ruta de la fuente (ej: `/run/media/usuario/CANON_DC/252_CANON/`)
- **-d** : Ruta del destino (ej: `/home/usuario/Imagenes/Fotos/`)

Formatos soportados:

- Imágenes: `.jpg`
- Videos : `.mp4`, `.avi`

---

## Estructura de salida

```
/home/usuario/Imagenes/Fotos/
└── 2014.11.12/
    ├── foto1.jpg
    ├── video1.mp4
    └── thumbs/
        ├── foto1_thumb.jpg
        └── video1_thumb.jpg
```

---

## Funcionamiento

1. **Lectura de metadatos**

   - Para fotos `.jpg`, se extrae la fecha EXIF (`DateTimeOriginal`)
   - Para videos `.mp4` y `.avi`, se usa la fecha de creación del archivo si no hay metadatos

2. **Creación de directorios**

   - Genera carpetas con nombre `YYYY.MM.DD` según la fecha de captura

3. **Generación de miniaturas**

   - Miniaturas con altura máxima de 100 píxeles, manteniendo la relación de aspecto
   - Guardadas en la subcarpeta `thumbs/`

4. **Copiado seguro**
   - Verifica duplicados y conserva los nombres originales

---

## Dependencias

Instalar con:

```bash
pip install pillow exifread
```

---

## Ejecución

Dar permisos:

```bash
chmod +x organizador_de_fotos.py
```

Ejecutar:

```bash
./organizador_de_fotos.py -s /ruta/fuente -d /ruta/destino
```

---

## Extracto de código

```python
import os, argparse, shutil
from PIL import Image
import exifread
from datetime import datetime

def obtener_fecha(f):
    with open(f, 'rb') as img:
        tags = exifread.process_file(img, stop_tag="EXIF DateTimeOriginal")
        date = tags.get("EXIF DateTimeOriginal")
    if date:
        return datetime.strptime(str(date), "%Y:%m:%d %H:%M:%S").strftime("%Y.%m.%d")
    else:
        return datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y.%m.%d")
```

---

## Conclusiones

- Automatiza la organización de grandes colecciones de fotos y videos
- Facilita la visualización rápida mediante miniaturas
- Diseño modular que permite extender a nuevos formatos

---

## Estructura del repositorio

```
organizador-de-fotos/
├── README.md
├── organizador_de_fotos.py
├── PATH_ORIGEN
└── PATH_DESTINO
```
