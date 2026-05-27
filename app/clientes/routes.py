from flask import request, render_template, redirect, url_for, Blueprint

from app.app import db
from app.clientes.models import Cliente

bp_clientes = Blueprint('bp_clientes', __name__, template_folder='templates')


@bp_clientes.route("/")
def index():

    clientes = Cliente.query.all()

    return render_template(
        'clientes/index.html',
        clientes=clientes
    )


@bp_clientes.route("/create", methods=['GET', 'POST'])
def create():

    if request.method == 'GET':

        return render_template('clientes/create.html')

    elif request.method == 'POST':

        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')

        # Crear un objeto clientes
        clientes = Cliente(
            nombre=nombre,
            telefono=telefono
        )

        # Insertar a la base de datos
        db.session.add(clientes)
        db.session.commit()

        # Redireccion al listado de clientess
        return redirect(url_for('bp_clientes.index'))


@bp_clientes.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    # Buscar el clientes por id
    clientes = Cliente.query.get_or_404(id)
    if request.method == 'GET':

        return render_template(
            'clientes/edit.html',
            clientes=clientes
        )
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')
      
        #Actualizacion de datos
        clientes.nombre = nombre
        clientes.telefono = telefono
        
        db.session.commit()

        # Redireccionar al listado
        return redirect(url_for('bp_clientes.index'))


@bp_clientes.route("/delete/<int:id>", methods=['POST'])
def delete(id):

    # Buscar el clientes
    clientes = Cliente.query.get_or_404(id)

    # Eliminar de la base de datos
    db.session.delete(clientes)
    db.session.commit()

    # Redireccionar al listado
    return redirect(url_for('bp_clientes.index'))