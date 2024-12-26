from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Curso import Cursos
from app import db

auth_bp= Blueprint('curso', __name__)

@auth_bp.route("/curso")
def index():
    data=Cursos()
    return render_template("curso/index.html", data = data)


@auth_bp.route("/curso/add", methods=["GET","POST"])  
def add():
    if request.method == 'POST':
        nombre            = request.form['nombre']
        descripcion       = request.form['descripcion']
        fechaInicio       = request.form['fechaInicio']
        fechaFin          = request.form['fechaFin']
        idInstructor      = request.form['idInstructor']
        
        newCurso = Cursos(nombre=nombre, descripcion=descripcion , fechaInicio=fechaInicio, fechaFin=fechaFin,idIntructor=idInstructor,)
        db.session.add(newCurso)
        db.session.commit()   
        
        return redirect(url_for('curso.index'))
    
    return render_template('curso/add.html')


@auth_bp.route("/curso/edit/<int:id>", methods=("GET","POST"))
def edit(id):
    curso = Cursos.query.get_or_404(id)
    if request.method         == 'POST':
        curso.nombre          = request.form['nombre']
        curso.descripcion     = request.form['descripcion']
        curso.fechaInicio     = request.form['fechaInicio']
        curso.fechaFin        = request.form['fechaFin']
        curso.idInstructor    = request.form['idInstructor']
        db.session.commit()
        
        return redirect(url_for('curso.index'))
    return render_template(url_for('curso/edit.html'))


@auth_bp.route("/curso/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    curso= Cursos.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    
    return render_template('curso/index.html')