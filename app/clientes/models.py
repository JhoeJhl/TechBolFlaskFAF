from app.app import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    #campos
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable = False)
    telefono = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"Nombre: {self.nombre} Telefono: {self.telefono}"
    
