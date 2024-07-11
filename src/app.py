from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import datetime, os


template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)



#- MySQL DB Config -#
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_cac'

mysql = MySQL(app)

#- Settings -#
app.secret_key = 'my_secret_key'


# Definición del modelo de Comentario
class Comentario:
    def __init__(self, id, nombre, correo, asunto, comentario, fecha, hora, fechaFormateada):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.asunto = asunto
        self.comentario = comentario
        self.fecha = fecha
        self.hora = hora
        self.fechaFormateada = fechaFormateada

# Definición de la clase Mensaje
class Mensaje:
    def __init__(self, id, nombre, apellido, email, telefono, asunto, comentario, checkk, fecha):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.asunto = asunto
        self.comentario = comentario
        self.checkk = checkk
        self.fecha = fecha


# Script para crear la tabla de Comentarios
with app.app_context():
    cursor = mysql.connection.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS comentarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                correo VARCHAR(50) NOT NULL,
                asunto VARCHAR(35) NOT NULL,
                comentario TEXT NOT NULL,
                fecha DATE NOT NULL,
                hora TIME NOT NULL,
                fechaFormateada VARCHAR(10) NOT NULL,
                fechaFormateadaEdit VARCHAR(10) NOT NULL,
                horaEdit TIME NOT NULL
            )
        ''')
            # Crear tabla Mensajes
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(30) NOT NULL,
                apellido VARCHAR(30) NOT NULL,
                email VARCHAR(60) NOT NULL,
                telefono VARCHAR(12) NOT NULL,
                asunto VARCHAR(60) NOT NULL,
                comentario TEXT NOT NULL,
                checkk TINYINT(1) NOT NULL,
                fecha DATETIME NOT NULL
            )
        ''')
    mysql.connection.commit()
    cursor.close()





#- Routes -#

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/candidatosYpropuestas')
def candidatosYpropuestas():
    return render_template('candYprop.html')


@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')

@app.route('/encuestaForm', methods=['POST'])
def encuestaForm():
    return redirect(url_for('encuesta'))


@app.route('/comentarios')
def comentarios():

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Comentarios ORDER BY CONCAT(fechaFormateada, ' ', hora) DESC")
        mi_resultado = cursor.fetchall()

        #- Convertir los datos a diccionario
        insertObject = []
        column_names = [column[0] for column in cursor.description]
        for row in mi_resultado:
            insertObject.append(dict(zip(column_names, row)))
        cursor.close()

        # Redirige a la página principal después de agregar el comentario
        return render_template('comentarios.html', data=insertObject)


@app.route('/agregarComentario', methods=['POST'])
def add_comentarios():
    if request.method == 'POST':

        fecha_hora = datetime.datetime.now()
        fecha_formateada = fecha_hora.strftime('%d/%m/%Y')
        hora = fecha_hora.strftime('%H:%M:%S')

        nombre = request.form['nombre']
        correo = request.form['correo']
        asunto = request.form['asunto']
        comentario = request.form['comentario']

        if nombre and correo and asunto and comentario:
            cur = mysql.connection.cursor()
            cur.execute("""INSERT INTO Comentarios (nombre, correo, asunto, comentario,
                        fecha, hora, fechaFormateada)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                        (nombre.strip(), correo.strip(), asunto.strip(), comentario.strip(),
                         fecha_hora, hora, fecha_formateada))

            # ! Puedo obtener los datos de la tabla con un print !
            #   print(fullname, phone, email)
            mysql.connection.commit()
            flash('Comentario agregado correctamente', 'success')  # Añade un mensaje flash de éxito
        else:
            flash('Por favor completa todos los campos', 'error')  # Mensaje flash de error si faltan campos

        # Redirige a la página principal después de agregar el comentario
        return redirect(url_for('comentarios'))  # 'main' es la función que renderiza 'index.html'

    # Si no es POST, simplemente redirige a la página principal
    return redirect(url_for('comentarios'))


@app.route('/borrar/<id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Comentarios WHERE id = {0}".format(id))
    mysql.connection.commit()
    flash('Contacto eliminado')
    return redirect(url_for('comentarios'))



@app.route('/editar/<id>') # <id> es similar a <string:id> - Simplemente no se le pasa el type a la funcion
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Comentarios WHERE id = {0}".format(id))
    data = cur.fetchall()
    contacto = data[0]
    print(contacto)
    return render_template('edit_contacto.html', contact=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':

        fecha_hora = datetime.datetime.now()
        fecha_formateadaEdit = fecha_hora.strftime('%d/%m/%Y')
        horaEdit = fecha_hora.strftime('%H:%M:%S')

        nombre = request.form['nombre']
        correo = request.form['correo']
        asunto = request.form['asunto']
        comentario = request.form['comentario']

        cur = mysql.connection.cursor()
        cur.execute("""
                    UPDATE Comentarios
                    Set nombre = %s,
                        correo = %s,
                        asunto = %s,
                        comentario = %s,
                        fechaFormateadaEdit = %s,
                        horaEdit = %s
                    WHERE id = %s
                    """, (nombre.strip(), correo.strip(), asunto.strip(), comentario.strip(),
                          fecha_formateadaEdit, horaEdit, id))
        mysql.connection.commit()
        # flash('Contacto actualizado')
        print("Contacto actualizado, redirigiendo a blog")
        return redirect(url_for('comentarios'))
    print("No se pudo actualizar el contacto")
    return "Error en la actualización"





@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')


@app.route('/mensajes_contacto', methods=['POST'])
def add_contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        asunto = request.form['asunto']
        comentario = request.form['comentario']
        checkk = request.form.get('checkk', False)
        checkk = True if checkk == 'on' else False  # Convierte a booleano
        fecha = datetime.datetime.now()

        if nombre and apellido and email and telefono and asunto and comentario:
            cur = mysql.connection.cursor()
            cur.execute("""INSERT INTO mensajes (nombre, apellido, email, telefono,
                        asunto, comentario, checkk, fecha)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                        (nombre.strip(), apellido.strip(), email.strip(), telefono.strip(),
                         asunto.strip(), comentario.strip(), checkk, fecha))

            # ! Puedo obtener los datos de la tabla con un print !
            #   print(fullname, phone, email)
            mysql.connection.commit()
            flash('Contacto agregado')
        return redirect(url_for('contactanos'))


if __name__ == "__main__":
    app.run(port=4000, debug=True)
