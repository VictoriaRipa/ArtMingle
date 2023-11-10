import unittest
from entidades.Imagen import Imagen

class Test(unittest.TestCase):

    @classmethod
    def test_contar_archivos_en_carpeta(cls):
            ruta="static/uploads"
            imagen = Imagen()
            imagen.contar_archivos_en_carpeta(ruta)


if __name__ == '__main__':
    unittest.main()
