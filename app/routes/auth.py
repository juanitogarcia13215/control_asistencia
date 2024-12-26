from flask import Blueprint, render_template, redirect, url_for, flash, Flask  
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/")
def index():
    return render_template("principal/index.html")



@auth_bp.route("/aprendiz")
def aprendiz():
    return render_template("aprendiz/index.html")

@auth_bp.route("/asistencia")
def asistencia():
    return render_template("asistencia/index.html")

@auth_bp.route("/principal")
def principal():
    return render_template("principal/index.html")

