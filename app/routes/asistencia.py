from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Asistencia import Asistencia
from app import db

auth_bp= Blueprint('asistencia', __name__)

@auth_bp.route("/asistencia")
def index():
    data=Asistencia.query.all()
    return render_template("asistencia/index.html", data = data)


@auth_bp.route("/asistencia/add", methods=["GET","POST"])  
def add():
    if request.method == 'POST':
        fecha         = request.form['fecha']
        estado        = request.form['estado']
        idCurso       = request.form['idCurso']
        idAprendiz    = request.form['idAprendiz']
        newAsistencia = Asistencia(fecha=fecha, est6ado=estado , idCurso=idCurso, idAprendiz=idAprendiz,)
        db.session.add(newAsistencia)
        db.session.commit()   
        
        return redirect(url_for('asistencia.index'))
    
    return render_template('asistencia/add.html')


@auth_bp.route("/asistencia/edit/<int:id>", methods=("GET","POST"))
def edit(id):
    asistencia = Asistencia.query.get_or_404(id)
    if request.method        == 'POST':
        asistencia.fecha       = request.form['fecha']
        asistencia.estado      = request.form['estado']
        asistencia.idCurso     = request.form['idCurso']
        asistencia.idAprendiz  = request.form['idAprendiz']
        db.session.commit()
        
        return redirect(url_for('asistencia.index'))
    return render_template(url_for('asistencia/edit.html'))


@auth_bp.route("/asistencia/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    asistencia= Asistencia.query.get_or_404(id)
    db.session.delete(asistencia)
    db.session.commit()
    
    return render_template('asistencia/index.html')