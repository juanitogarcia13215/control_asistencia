from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Curso import Cursos
from app.models.Instructor import Instructor
from datetime import datetime
from app import db

auth_bp= Blueprint('curso', __name__)

@auth_bp.route("/curso")
def index():
    curso = Cursos.query.all()
    instructor = Instructor.query.all()
    return render_template("curso/index.html", curso = curso, instructor=instructor )


@auth_bp.route("/curso/add", methods=["GET","POST"])  
def add():
    if request.method == 'POST':
        nombre            = request.form['nombre']
        descripcion       = request.form['descripcion']
        fechaInicio  = datetime.strptime(request.form['fechaInicio'], '%Y-%m-%d').date()
        fechaFin     = datetime.strptime(request.form['fechaFin'], '%Y-%m-%d').date()
        idInstructor      = request.form['idInstructor']
    
        
        newCurso = Cursos(nombre=nombre, descripcion=descripcion , fechaInicio=fechaInicio, fechaFin=fechaFin, idInstructor=idInstructor)
        db.session.add(newCurso)
        db.session.commit()   
        
        return redirect(url_for('curso.index'))
    instructor= Instructor.query.all()
    
    return render_template('curso/add.html',  instructores=instructor)


@auth_bp.route("/curso/edit/<int:id>", methods=("GET","POST"))  
def edit(id):
    curso = Cursos.query.get_or_404(id)
    if request.method         == 'POST':
        curso.nombre          = request.form['nombre']
        curso.descripcion     = request.form['descripcion']
        curso.fechaInicio  = datetime.strptime(request.form['fechaInicio'], '%Y-%m-%d').date()
        curso.fechaFin     = datetime.strptime(request.form['fechaFin'], '%Y-%m-%d').date()
        curso.idInstructor    = request.form['idInstructor']
        db.session.commit()
        
        return redirect(url_for('curso.index'))
    instructor = Instructor.query.all()
    return render_template('curso/edit.html', curso=curso, instructores=instructor)


@auth_bp.route("/curso/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    curso= Cursos.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    
    return render_template('curso/index.html')