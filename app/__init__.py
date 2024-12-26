from flask import Flask, redirect, url_for,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from config import Config

# Instanciación de extensiones
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()


def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_object(Config)  # Carga la configuración desde config.py
    app.config['SECRET_KEY']   # Genera un SECRET_KEY

    # Inicialización de extensiones
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Importación de los modelos (asegúrate de que se importen aquí)
#---------------------------------------CREACION DE LAS TABLAS DE LA BASE DE DATOS
    from app.models import Aprendiz,Asistencia,Curso,Instructor
    
    
#-----------------------------------------------------FIN
    # Configuración de Flask-Login
    login_manager.login_view = 'auth.login'  # Vista de inicio de sesión
    login_manager.login_message = "Por favor, inicie sesión para acceder a esta página."

    @login_manager.user_loader
    def load_user(user_id):
        return aprendiz.query.get(int(user_id))

    # Registro de Blueprints
    from app.routes import auth,aprendiz,asistencia,curso,instructor
    
    app.register_blueprint(auth.auth_bp),
    app.register_blueprint(aprendiz.auth_bp)
    app.register_blueprint(asistencia.auth_bp)
    app.register_blueprint(curso.auth_bp)
    app.register_blueprint(instructor.auth_bp)
   
    
    return app
