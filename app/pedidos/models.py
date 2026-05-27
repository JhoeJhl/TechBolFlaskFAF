from app.app import db
from datetime import datetime

class Pedido(db.Model):

    __tablename__ = "pedidos"

    # Campos
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date,nullable=False)
    monto = db.Column(db.Float,nullable=False)

    # Foreign Keys
    producto_id = db.Column( db.Integer,db.ForeignKey('productos.id'),nullable=False)
    cliente_id = db.Column(db.Integer,db.ForeignKey('clientes.id'),nullable=False)

    #relaciones 
    cliente = db.relationship('Cliente', back_populates = 'pedidos')
    producto = db.relationship('Producto', back_populates = 'pedidos')


    def __repr__(self):
        return f"Fecha: {self.fecha} | Monto: {self.monto} | Cliente: {self.cliente_id} | Producto: {self.producto_id}"