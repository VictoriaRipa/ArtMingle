import os

class Imagen:

    ruta = "static/uploads"

    def contar_archivos_en_carpeta(self,ruta):
        if os.path.exists(ruta) and os.path.isdir(ruta):
            archivos = os.listdir(ruta)
            cantidad_de_archivos = len(archivos)
            return "La cantidad de Imagenes disponibles son " + str(cantidad_de_archivos)
        else:
            return "todavia no hay imagenes cargadas"