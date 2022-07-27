#libreria que permite leer los archivos
import os 
#libreria que nos permite comprimir las imagenes
from PIL import Image 

#directorio donde se buscan los archivos
downloadsFolder = "C:/Users/N.A.H/Documents/Cursos/Python/Compressor/"

if __name__ == "__main__":
    #iteramos todos los archivos que se encuentran dentro de la carpeta
    for filename in os.listdir(downloadsFolder):
        #separamos el nombre del archivo y su extension
        name, extension = os.path.splitext(downloadsFolder + filename)
        #con un condicional verificamos si su extension es jpg, jpeg o png
        if extension in [".jpg", ".jpeg",".png"]:
            #si es true abrimos la imagen
            picture = Image.open(downloadsFolder + filename)
            #guardamos dentro de la misma carpeta, le agregamos el sring al comiento del nombre, el parametro optimize en true y la calidad que queremos
            print(downloadsFolder)
            print(downloadsFolder + "compressed_" + filename)
            picture.save(downloadsFolder + "compressed_" + filename, optimize=True, quality=60)
