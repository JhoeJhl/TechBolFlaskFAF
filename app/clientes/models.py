from app.app import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    #campos
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable = False)
    telefono = db.Column(db.String(20), nullable = False)

    #relacion con pedidos
    pedidos = db.relationship('Pedido', back_populates = 'cliente')


    def __repr__(self):
        return f"Nombre: {self.nombre} Telefono: {self.telefono}"
    
