import mysql.connector

# Conectarse a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="redsocial",
    port=3306
)

class Usuario:
    def __init__(self, idUsuarios,nombre, apellido, email, contraseña):
        self.idUsuarios=idUsuarios
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejemplo de inserción de datos en la tabla 'usuarios'
nuevo_usuario = Usuario(3,"tato", "fazio", "tatofa43@gmail.com", "tatoo01")

# Consulta SQL para insertar datos
sql = "INSERT INTO usuarios (idusuarios,nombre, apellido, email, clave) VALUES (%s,%s, %s, %s, %s)"

# Valores a insertar
valores = (nuevo_usuario.idUsuarios,nuevo_usuario.nombre, nuevo_usuario.apellido, nuevo_usuario.email, nuevo_usuario.contraseña)

try:
    # Ejecutar la consulta SQL
    cursor.execute(sql, valores)

    # Confirmar la inserción de datos
    conexion.commit()
    print("Datos insertados correctamente")
except mysql.connector.Error as error:
    print(f"Error al insertar datos: {error}")
finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
