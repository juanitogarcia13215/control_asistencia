from app import db

class Cursos(db.Model):
    __tablename__='curso'
    idCurso      = db.Column(db.Integer,primary_key=True)
    nombre       = db.Column(db.String(255), nullable=False)
    descripcion  = db.Column(db.String(255),   nullable=False)
    fechaInicio  = db.Column(db.Date, nullable=False)
    fechaFin     = db.Column(db.Date, nullable=False)
    idInstructor = db.Column(db.Integer,db.ForeignKey('instructor.idInstructor'), nullable=False)
    
    
    def create_tables():
        db.create_all()