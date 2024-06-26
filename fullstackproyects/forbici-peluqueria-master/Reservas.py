from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reservas (db.Model):
    
    __tablename__="reservas"
    
    id = db.Column (db.Integer, primary_key=True)
    nombre = db.Column (db.String(50))
    numero = db.Column (db.String(50))
    fecha = db.Column (db.String(50))
    hora = db.Column (db.String(50))
    servicio = db.Column (db.String(50))
    email = db.Column (db.String(50))
    
    def __init__(self,nombre,numero,fecha,hora,servicio,email):
        
        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.email = email

class Reserva_Productos (db.Model):
    
    __tablename__="reservas_productos"
    __bind_key__="reservas_productos"
    
    id = db.Column (db.Integer, primary_key=True)
    nombre = db.Column (db.String(50))
    numero = db.Column (db.String(50))
    producto = db.Column (db.String(50))
    email = db.Column (db.String(50))
    
    def __init__(self,nombre,numero,producto,email):
        
        self.nombre = nombre
        self.numero = numero
        self.producto = producto
        self.email = email