from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    print("Creating Flask app...")
    app.config.from_object('config.Config')

    db.init_app(app)
    csrf.init_app(app)
    print("Initialized extensions...")

    with app.app_context():
        # Import Blueprints
        print("Importing routes...")
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)
        print("Registered blueprints...")

        return app
