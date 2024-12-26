from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Aprendiz import Aprendiz
from app.models.Curso import Cursos
from app import db

auth_bp= Blueprint('aprendiz', __name__)

@auth_bp.route("/aprendiz")
def index():
    aprendiz=Aprendiz.query.all()
    print(aprendiz)  # Verifica si contiene los registros

    return render_template("aprendiz/index.html", aprendiz = aprendiz)


@auth_bp.route("/aprendiz/add", methods=["GET","POST"])  
def add():
    if request.method == 'POST':
        nombre    = request.form['nombre']
        correo    = request.form['correo']
        documento = request.form['documento']
        telefono  = request.form['telefono']
        idCurso   = request.form['idCurso']
        newAprendiz = Aprendiz(nombre= nombre, correo=correo , documento=documento, telefono=telefono, idCurso=idCurso)
        db.session.add(newAprendiz)
        db.session.Commit()   
        curso = Cursos.query.filter_by(nombre='nombreCurso').first()
        
        return redirect(url_for('aprendiz.index', curso = curso))
    
    return render_template('aprendiz/add.html')


@auth_bp.route("/aprendiz/edit/<int:id>", methods=("GET","POST"))
def edit(id):
    aprendiz = Aprendiz.query.get_or_404(id)
    if request.method == 'POST':
        aprendiz.nombre = request.form['nombre']
        aprendiz.correo = request.form['correo']
        aprendiz.documento = request.form['documento']
        aprendiz.telefono = request.form['telefono']
        aprendiz.idCurso = request.form['idCurso']
        
        db.session.commit
        return redirect(url_for('aprendiz.index'))
    return render_template(url_for('aprendiz/edit.html'))


@auth_bp.route("/aprendiz/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    aprendiz= Aprendiz.query.get_or_404(id)
    db.session.delete(aprendiz)
    db.session.commit()
    
    return render_template('aprendiz/indez.html')