from app import db

class Asistencia(db.Model):
    __tablename__='asistencia'
    idAsistencia = db.Column(db.Integer,primary_key=True)
    fecha        = db.Column(db.Date, nullable=False)
    estado       = db.Column(db.String(255), nullable = False,)
    idCurso      = db.Column(db.Integer, db.ForeignKey("curso.idCurso"), nullable=False,)
    idAprendiz   = db.Column(db.Integer, db.ForeignKey('aprendiz.idAprendiz'),nullable=False,)
    
    def create_tables():
        db.create_all()
    
    
    
    