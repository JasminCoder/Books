from flask_app import app
from flask import redirect, render_template, request
from ..models.autores import Autor
from flask_app.models.libros import Libro
#linea 3 y 4 es lo mismo, se puede escribir de ambas formas


#ruta raiz
@app.route('/')
def index():
    return redirect('/autores')


#ruta autores
@app.route('/autores')
def autores():
    autores = Autor.mostrar_autores()
    return render_template('autores.html', autores=autores)


#ruta guardar autor
@app.route('/guardar/autor', methods=['POST'])
def guardar_autor():
    data = {
        "nombre": request.form['nombre']
    }
    nuevo_autor = Autor.guardar_autor(data)
    return redirect('/autores')


#mostrar info del autor
@app.route('/autor/<int:id>')
def mostar_autor(id):
    data = {
        "id": id
    }
    autor = Autor.mostrar_autor(data)
    libros_no_favoritos = Libro.libros_no_favoritos(data)
    return render_template('mostrar_autor.html', autor=autor, libros_no_favoritos=libros_no_favoritos)



#ruta guardar favoritos
@app.route('/guardar/favorito', methods=['POST'])
def guardar_libro_favorito():
    data = {
        'autor_id': request.form['autor_id'],
        'libro_id': request.form['libro_id']
    }

    Autor.nuevo_favorito(data)
    return redirect(f"/autor/{request.form['autor_id']}")