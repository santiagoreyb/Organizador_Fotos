#!/usr/bin/env python
import sys
import PIL
import os
import datetime
from PIL import Image
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Es necesario colocar argumento fuente y argumento destino")
    else:
        if sys.argv[1] == '-s':
            fuente = sys.argv[2]
            print("fuente: ", fuente)
        if sys.argv[3] == '-d':
            dest = sys.argv[4]
            print("destino: ", dest)
contenido = os.listdir(fuente)
archivos = []
for fichero in contenido:
    if os.path.isfile(os.path.join(fuente, fichero)) and fichero.endswith('.jpg'):
        archivos.append(fichero)
    if os.path.isfile(os.path.join(fuente, fichero)) and fichero.endswith('.mp4'):
        archivos.append(fichero)
    if os.path.isfile(os.path.join(fuente, fichero)) and fichero.endswith('.avi'):
        archivos.append(fichero)
for i in archivos:
    fecha_archivo = os.path.getatime(i)
    destino = dest + '/' + fecha_archivo.year + '.' + fecha_archivo.month + '.' + fecha_archivo.day
    try:
        os.mkdir(destino)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    i.save(destino)
    destinothumb = destino + '/thumbs'
    try:
        os.mkdir(destinothumb)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    img = i.resize((100, 100), Image.ANTIALIAS)
    img.save(destinothumb)
