import sqlite3 as sql
class Conexion:

    def __init__(self, nombreBD):
      self.conexion = sql.connect(nombreBD)
      self.cursor = self.conexion.cursor()


    def crearTablaPublicacion(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS `publicaciones` (`id_publicaciones` INTEGER PRIMARY KEY AUTOINCREMENT,`contenido` TEXT NOT NULL,`pieDeFoto` TEXT NOT NULL,`recuentoDeLikes` INTEGER NOT NULL)''')
        self.conexion.commit()

    def crearT_US_Publi(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS `usuarios_has_publicaciones` (`usuarios_idusuarios` INTEGER NOT NULL,`publicaciones_id_publicaciones` INTEGER NOT NULL,PRIMARY KEY (`usuarios_idusuarios`, `publicaciones_id_publicaciones`),FOREIGN KEY (`usuarios_idusuarios`) REFERENCES `usuarios` (`idusuarios`) ON DELETE NO ACTION ON UPDATE NO ACTION,FOREIGN KEY (`publicaciones_id_publicaciones`) REFERENCES `publicaciones` (`id_publicaciones`) ON DELETE NO ACTION ON UPDATE NO ACTION)''')
        self.conexion.commit()

    def crearTablaComentarios(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS comentarios (idcomentarios INTEGER PRIMARY KEY AUTOINCREMENT, comentario TEXT NOT NULL, publicaciones_id_publicaciones INTEGER, FOREIGN KEY (publicaciones_id_publicaciones) REFERENCES publicaciones (id_publicaciones) ON DELETE NO ACTION ON UPDATE NO ACTION);''')
        self.conexion.commit()

    def insertarRegistroPublicacion(self, contenido, pieDeFoto, recuentoDeLikes):
        self.cursor.execute("INSERT INTO publicaciones (contenido, pieDeFoto, recuentoDeLikes) VALUES (?, ?, ?)",
                            (contenido, pieDeFoto, recuentoDeLikes))
        self.conexion.commit()

    def insertarRelacionUsuarioPublicacion(self, idUsuario, idPublicacion):
        self.cursor.execute(
            "INSERT INTO usuarios_has_publicaciones (usuarios_idusuarios, publicaciones_id_publicaciones) VALUES (?, ?)",
            (idUsuario, idPublicacion))
        self.conexion.commit()

    def insertarComentario(self, comentario, idPublicacion):
        self.cursor.execute("INSERT INTO comentarios (comentario, publicaciones_id_publicaciones) VALUES (?, ?)",
                            (comentario, idPublicacion))
        self.conexion.commit()

    def cerrarConexion(self):
        self.cursor.close()
        self.conexion.close()
