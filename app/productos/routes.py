from flask import request, render_template, redirect, url_for, Blueprint

from app.app import db
from app.productos.models import Producto

bp_productos = Blueprint('bp_productos',__name__,template_folder='templates')

@bp_productos.route("/")
def index():

    productos = Producto.query.all()

    return render_template('productos/index.html',productos=productos)


@bp_productos.route("/create", methods=['GET', 'POST'])
def create():

    if request.method == 'GET':

        return render_template('productos/create.html')

    elif request.method == 'POST':

        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        stock = request.form.get('stock')

        # Crear objeto producto
        producto = Producto(nombre=nombre,precio=precio,stock=stock)

        # Guardar en la base de datos
        db.session.add(producto)
        db.session.commit()

        return redirect(url_for('bp_productos.index'))


@bp_productos.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):

    # obtenemos el producto
    producto = Producto.query.get_or_404(id)

    if request.method == 'GET':

        return render_template(
            'productos/edit.html',
            producto=producto
        )

    elif request.method == 'POST':

        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        stock = request.form.get('stock')

        # Actualizar datos
        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock

        db.session.commit()

        # Redireccionar
        return redirect(url_for('bp_productos.index'))


@bp_productos.route("/delete/<int:id>", methods=['POST'])
def delete(id):

    # Buscar producto
    producto = Producto.query.get_or_404(id)

    # Eliminar
    db.session.delete(producto)
    db.session.commit()

    # Redireccionar
    return redirect(url_for('bp_productos.index'))