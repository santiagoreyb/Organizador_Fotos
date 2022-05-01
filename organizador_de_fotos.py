import cv2
import sys
import PIL
import os
import datetime
import time
from PIL import Image
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Es necesario colocar argumento fuente y argumento destino!")
    else:
        if sys.argv[1] == '-s':
            fuente = sys.argv[2]
            print("fuente.: ", fuente)
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
    farchivo = fuente + "/" + i
    fecha_ar = time.ctime(os.path.getctime(farchivo))
    obj = time.strptime(fecha_ar)
    fecha_archivo = time.strftime("%Y.%m.%d",obj)
    destino = dest + '/' + fecha_archivo
    if not os.path.exists(destino):
        os.makedirs(destino)
        print("Directorio creado: ", destino)
    destinothumb = destino + '/thumbs' 
    if not os.path.exists(destinothumb):
        os.makedirs(destinothumb)
        print("Directorio thumb creado: ", destinothumb) 
    os.replace(farchivo, destino + "/" + i)
    img2 = cv2.imread(destino + "/" + i)
    img2resize = cv2.resize(img2, (100,100))  
    cv2.imwrite(destinothumb + "/" + i, img2resize)
print("Proceso terminado!!!")
   
