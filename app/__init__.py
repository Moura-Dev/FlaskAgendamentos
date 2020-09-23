from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:itnisanjr19@localhost/consultas'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    migrate = Migrate(app, db)

    from .views import main
    app.register_blueprint(main)

    return app