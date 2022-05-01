#!/usr/bin/env python
import sys
import PIL
import os
import cv2
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
'''
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
'''



for file_name in files_names:
    #print(file_name)

    if file_name.split(".")[-1] not in ["jpeg", "mp4", "jpg", "avi"]:
        continue
    fecha_archivo = os.path.getatime(i)
    destino = dest + '/' + fecha_archivo.year + '.' + fecha_archivo.month + '.' + fecha_archivo.day    
    if not os.path.exists(destino):
        os.makedirs(destino)
        print("Directorio creado: ", destino)
    destinothumb = destino + '/thumbs' 
    if not os.path.exists(destinothumb):
        os.makedirs(destinothumb)
        print("Directorio thumb creado: ", destinothumb)
    image_path = fuente + "/" + file_name
    image = cv2.imread(image_path)
    if image is None:
        continue
    cv2.imwrite(destino, image)
    image2 = cv2.imread(image_path)
    if image2 is None:
        continue
    image2 = cv2.resize(image2, (100, 100), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(destinothumb, image2)
