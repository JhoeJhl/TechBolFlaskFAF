from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()



def create_app():

    app = Flask(__name__, template_folder='templates')
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///bd_equipo.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    #1. Importacion del blueprint (Para cada modulo)
    from app.clientes.routes import bp_clientes
    from app.pedidos.routes import bp_pedidos
    from app.productos.routes import bp_productos
    from app.core.routes import bp_core
    

    #2. Registrar el blueprint (Para cada modulo)
    app.register_blueprint(bp_clientes, url_prefix="/miembros")
    app.register_blueprint(bp_pedidos, url_prefix="/pedidos")
    app.register_blueprint(bp_productos, url_prefix="/productos")
    app.register_blueprint(bp_core, url_prefix="/")
    
    return app

    
