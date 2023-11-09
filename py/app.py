from flask import Flask, render_template, request, url_for, redirect
import os
from entidades.Imagen import Imagen
from  entidades.Usuario import Usuario


app = Flask(__name__)

# Ruta para mostrar el formulario de carga
@app.route('/')
def index():
    img = Imagen()
    image_files, cantidadImg = img.obtener_ultimas_imagenes()
    return render_template('index.html', image_files=image_files, cantidadImg=cantidadImg)


@app.route('/upload')
def upload_form():
    return render_template('upload.html')

# Ruta para manejar la carga de la imagen
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No se ha seleccionado ningún archivo."

    file = request.files['file']

    if file.filename == '':
        return "No se ha seleccionado ningún archivo."

    if file:
        # Procesar la imagen aquí
        # Por ejemplo, puedes guardarla en una carpeta en el servidor
        file.save('static/uploads/' + file.filename)  # Asegúrate de tener una carpeta 'uploads' creada

        # Redireccionar a la página que muestra las imágenes
        return redirect(url_for('mostrar_publicaciones'))

# Ruta para ver las imágenes que hay
@app.route('/mostrar')
def mostrar_publicaciones():
    img = Imagen()
    image_files, cantidadImg = img.obtener_ultimas_imagenes()
    return render_template('mostrarImgs.html', cantidadImg=cantidadImg, image_files=image_files)
    # Obtén la lista de nombres de archivo de las imágenes en la carpeta "uploads"
    image_folder = "static/uploads"
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    # Renderiza la plantilla HTML y pasa la lista de nombres de archivo



@app.route('/perfil', methods=["GET","POST"])
def infoPerfil():
    if request.method == "POST":
        usuario = request.form["nombreUsuario"]
        email = request.form["email"]
        clave=request.form["contraseña"]
        us=Usuario("DataBase/baseDatos.db")
        us.insertarRegistroUsuario(usuario,email,clave)
        return redirect(url_for("resultados", usuario=usuario, email=email))

    return render_template('registro.html')

@app.route('/resultado')
def resultados():
    usuario = request.args.get("usuario")
    email = request.args.get("email")
    return render_template("resultados.html", usuario=usuario, email=email)



if __name__ == '__main__':
    app.run(debug=True)


