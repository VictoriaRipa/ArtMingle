from entidades.Conexion import Conexion

class Usuario:
    def __init__(self, nombreBD):
        self.nombre_usuario = ""
        self.email = ""
        self.clave = ""
        self.con = Conexion(nombreBD)




    def crearTablaUsuario(self):
       self.con.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                idusuarios INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_usuario TEXT NOT NULL,
                email TEXT NOT NULL,
                clave TEXT NOT NULL
            )
        ''')
       self.con.conexion.commit()

    def insertarRegistroUsuario(self, nombre_usuario, email, clave):
        if nombre_usuario  and email and clave:
            self.con.cursor.execute("INSERT INTO usuarios (nombre_usuario, email, clave) VALUES (?, ?, ?)",
                                (nombre_usuario,email, clave))
            self.con.conexion.commit()
            print("Datos insertados en la base de datos.")
        else:
            print("Por favor, complete todos los campos.")

    def actualizarRegistroUsuario(self, id_usuario, nombre_usuario, email, clave):
        if nombre_usuario and  email and clave:
            self.con.cursor.execute("UPDATE usuarios SET nombre_usuario=?, email=?, clave=? WHERE idusuarios=?",
                                (nombre_usuario, email, clave, id_usuario))
            self.con.conexion.commit()
            print("Datos actualizados en la base de datos.")
        else:
            print("Por favor, complete todos los campos.")

    def borrarUsuario(self, id_usuario):
        self.con.cursor.execute("DELETE FROM usuarios WHERE idusuarios=?", (id_usuario,))
        self.con.conexion.commit()
        print("Registro eliminado de la base de datos.")

    def mostrarRegistros(self):
        self.con.cursor.execute("SELECT * FROM usuarios")
        registros = self.con.cursor.fetchall()

        for registro in registros:
            print(
                f"id_usuario: {registro[0]}, nombre_usuario: {registro[1]}, Email: {registro[2]}, clave: {registro[3]}")