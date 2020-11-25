from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    role = db.Column(db.Enum("Administrador", "Empleado", "Usuario"))
    room_relathionship = db.relationship("Room", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "role": self.role,
        }

class Room(db.Model):
    __tablename__= "room"
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(255), nullable=False)
    coworking = db.Column(db.String(255), unique=False, nullable=False)
    capacity = db.Column(db.Integer, unique=False, nullable=False)
    disinfection = db.Column(db.Integer, unique=False, nullable=True)
    ventilation = db.Column(db.Integer, unique=False, nullable=True)
    username = db.Column(db.String(80), ForeignKey("user.username"))
    
    def serialize(self):
        return {
            "id": self.id,
            "coworking": self.coworking,
            "capacity": self.capacity,
            "disinfection": self.disinfection,
            "ventilation": self.ventilation
        }

class Code(db.Model):
    __tablename__ = "code"
    code = db.Column(db.Integer, primary_key=True)

    def serialize(self):
        return {
            "code": self.code
        }

