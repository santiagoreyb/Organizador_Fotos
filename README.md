# 📸 Organizador de Fotos (versión OpenCV)

Autor: Santiago Camilo Rey Benavides  
Pontificia Universidad Javeriana – Ingeniería de Sistemas  

------------------------------------------------------------
## Descripción General
Script en **Python 3** que organiza fotos y videos en carpetas
según la **fecha de creación del archivo**.  
Además, genera una carpeta `thumbs` con **miniaturas de 100x100 píxeles**
para cada archivo.

Usa **OpenCV** para redimensionar imágenes y la librería estándar de Python
para manejar directorios y fechas.

------------------------------------------------------------
## Requisitos
- Python 3
- Librerías:
  - opencv-python (`cv2`)
  - Pillow (`PIL`)

Instalación de dependencias:
```
pip install opencv-python pillow
```

------------------------------------------------------------
## Uso
Ejecutar desde la terminal:
```
./organizador_de_fotos.py -s <ruta_fuente> -d <ruta_destino>
```
Ejemplo:
```
./organizador_de_fotos.py -s /run/media/usuario/CANON_DC/252_CANON/ -d /home/usuario/Imagenes/Fotos/
```

Parámetros:
- **-s** : Carpeta de origen (memoria de la cámara, disco, etc.)
- **-d** : Carpeta destino donde se organizarán las fotos y videos.

------------------------------------------------------------
## Formatos soportados
- Imágenes: `.jpg`
- Videos : `.mp4`, `.avi`

------------------------------------------------------------
## Funcionamiento del código
1. **Validación de argumentos**
   Verifica que se ingresen las rutas `-s` y `-d`.
   Si no, muestra un mensaje de error.

2. **Búsqueda de archivos**
   Recorre la carpeta de origen y filtra solo archivos `.jpg`, `.mp4`, `.avi`.

3. **Organización por fecha**
   - Toma la fecha de creación del archivo (`os.path.getctime`).
   - Formatea la fecha como `YYYY.MM.DD`.
   - Crea una carpeta con esa fecha dentro de la ruta destino.

4. **Creación de miniaturas**
   - Dentro de cada carpeta de fecha crea `thumbs/`.
   - Redimensiona cada imagen o cuadro de video a **100x100 píxeles** con OpenCV.
   - Guarda el archivo con el mismo nombre en `thumbs/`.

5. **Mover archivos**
   - Usa `os.replace` para mover el archivo original a su carpeta de fecha.

6. **Mensajes en consola**
   - Muestra cada carpeta creada y finaliza con:
     `Proceso terminado!!!`

------------------------------------------------------------
## Estructura de salida
```
<destino>/
└── 2025.09.17/
    ├── foto1.jpg
    ├── video1.mp4
    └── thumbs/
        ├── foto1.jpg
        └── video1.jpg
```

------------------------------------------------------------
## Notas
- El script mueve los archivos **originales** al destino (no copia).
- Las miniaturas se generan a tamaño **100x100 píxeles** fijos.
- Para videos, solo se guarda una imagen redimensionada del primer cuadro
  (si el archivo es compatible con OpenCV).

------------------------------------------------------------
## Estructura del repositorio
```
organizador-de-fotos/
├── README.txt
└── organizador_de_fotos.py
```
├── PATH_ORIGEN
└── PATH_DESTINO
```
