from flask_login import UserMixin
from app import db

class Aprendiz(db.Model,UserMixin):
    __tablename__='aprendiz'
    idAprendiz = db.Column(db.Integer,primary_key=True)
    nombre     = db.Column(db.String(255), nullable=False)
    correo     = db.Column(db.String(255),  unique=True, nullable=False)
    documento  = db.Column(db.String(255), nullable=False)
    telefono   = db.Column(db.String(255), nullable=False)
    idCurso    = db.Column(db.Integer,db.ForeignKey('curso.idCurso'), nullable=False)
   
   
    def create_tables():
        db.create_all()
    
    
    
    
    