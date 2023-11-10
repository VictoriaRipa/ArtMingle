import os

import os

class Imagen:
    ruta = "static/uploads"

    def obtener_ultimas_imagenes(self):
        ruta = self.ruta
        if os.path.exists(ruta) and os.path.isdir(ruta):
            archivos = os.listdir(ruta)
            archivos = sorted(archivos, key=lambda x: os.path.getctime(os.path.join(ruta, x)), reverse=True)
            cantidad_de_archivos = len(archivos)
            return archivos, cantidad_de_archivos
        else:
            return [], 0