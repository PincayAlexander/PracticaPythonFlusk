from flask import Flask
from app.database.db import init_database
from app.modules.books import bookBp
from dotenv import load_dotenv
import os

load_dotenv()
    
# App con flask
app = Flask(__name__)

def init_app():
    # Ajustes
    app.config['DEBUG'] = True 
    app.secret_key = os.getenv('SECRET_KEY') or  "secret-123key"

    # Iniciar base de datos
    init_database(app)

    # Rutas
    app.register_blueprint(bookBp)
    return app
