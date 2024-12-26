from app.models.Instructor import db, Instructor
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db

auth_bp= Blueprint('instructor', __name__)

@auth_bp.route("/instructor")
def index():
    data=Instructor()
    return render_template("instructor/index.html", data = data)


@auth_bp.route("/instructor/add", methods=["GET","POST"])  
def add():
    if request.method == 'POST':
        nombre             = request.form['nombre']
        correo             = request.form['correo']
        documento          = request.form['documento']
        especializacion     = request.form['especializacion']
        telefono           = request.form['telefono']
        
        newinstructor = Instructor(nombre=nombre, correo=correo , documento=documento, especializacion=especializacion,telefono=telefono,)
        db.session.add(newinstructor)
        db.session.commit()   
        
        return redirect(url_for('instructor.index'))
    
    return render_template('instructor/add.html')


@auth_bp.route("/instructor/edit/<int:id>", methods=("GET","POST"))
def edit(id):
    instructor = Instructor.query.get_or_404(id)
    if request.method         == 'POST':
        instructor.nombre             = request.form['nombre']     
        instructor.correo             = request.form['correo']
        instructor.documento          = request.form['documento']
        instructor.especializacion    = request.form['especializacion']
        instructor.telefono           = request.form['telefono']
        db.session.commit()
        
        return redirect(url_for('instructor.index'))
    return render_template(url_for('instructor/edit.html'))


@auth_bp.route("/instructor/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    instructor= Instructor.query.get_or_404(id)
    db.session.delete(instructor)
    db.session.commit()
    
    return render_template('instructor/index.html')