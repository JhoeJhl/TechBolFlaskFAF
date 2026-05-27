from flask import request, render_template, redirect, url_for, Blueprint

from app.app import db
from app.pedidos.models import Pedido
from app.clientes.models import Cliente
from app.productos.models import Producto

bp_pedidos = Blueprint('bp_pedidos',__name__,template_folder='templates')

@bp_pedidos.route("/")
def index():

    pedidos = Pedido.query.all()

    return render_template(
        'pedidos/index.html',
        pedidos=pedidos
    )


@bp_pedidos.route("/create", methods=['GET', 'POST'])
def create():

    if request.method == 'GET':

        clientes = Cliente.query.all()
        productos = Producto.query.all()

        return render_template('pedidos/create.html',clientes=clientes,productos=productos)

    elif request.method == 'POST':

        fecha = request.form.get('fecha')
        monto = request.form.get('monto')
        cliente_id = request.form.get('cliente_id')
        producto_id = request.form.get('producto_id')

        # Crear objeto pedido
        pedido = Pedido(fecha=fecha, monto=monto,cliente_id=cliente_id,producto_id=producto_id)

        # Insertar en base de datos
        db.session.add(pedido)
        db.session.commit()

        # Redireccionar
        return redirect(url_for('bp_pedidos.index'))


@bp_pedidos.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):

    # Buscar pedido
    pedido = Pedido.query.get_or_404(id)

    if request.method == 'GET':

        clientes = Cliente.query.all()
        productos = Producto.query.all()

        return render_template(
            'pedidos/edit.html',
            pedido=pedido,
            clientes=clientes,
            productos=productos
        )

    elif request.method == 'POST':

        fecha = request.form.get('fecha')
        monto = request.form.get('monto')
        cliente_id = request.form.get('cliente_id')
        producto_id = request.form.get('producto_id')

        # Actualizar datos
        pedido.fecha = fecha
        pedido.monto = monto
        pedido.cliente_id = cliente_id
        pedido.producto_id = producto_id

        db.session.commit()

        # Redireccionar
        return redirect(url_for('bp_pedidos.index'))


@bp_pedidos.route("/delete/<int:id>", methods=['POST'])
def delete(id):

    # Buscar pedido
    pedido = Pedido.query.get_or_404(id)

    # Eliminar
    db.session.delete(pedido)
    db.session.commit()

    # Redireccionar
    return redirect(url_for('bp_pedidos.index'))