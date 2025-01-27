from flask_login import UserMixin
from app import db

class Instructor(db.Model,UserMixin):
    __tablename__='instructor'
    idInstructor = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255),  unique=True, nullable=False)
    documento = db.Column(db.String(255), nullable=False)
    especializacion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
   
    
    def get_id(self):
        return str(self.idInstructor)
   
    def create_tables():
        db.create_all()