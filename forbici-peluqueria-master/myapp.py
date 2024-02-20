from flask import *
from Reservas import db
from Reservas import Reservas 
from Reservas import Reserva_Productos


class Forbici:
    
    def __init__ (self):
        
        self.app = Flask(__name__)
        self.app.config ['SQLALCHEMY_DATABASE_URI']='sqlite:///reservasforbici.sqlite3'
        self.app.config ['SQLALCHEMY_BINDS']={'reservas_productos':'sqlite:///reservasproductosforbici.sqlite3'}
        
        db.init_app(self.app)
        
        self.app.add_url_rule('/', view_func=self.inicio)
        self.app.add_url_rule('/damas', view_func=self.damas)
        self.app.add_url_rule('/caballeros', view_func=self.caballeros)
        self.app.add_url_rule('/marcel_france', view_func=self.marcel_france)
        self.app.add_url_rule('/reserva/<servicio>', view_func=self.reserva, methods=["GET","POST"])
        self.app.add_url_rule('/reserva_producto/<producto>', view_func=self.reserva_producto, methods=["GET","POST"])
        
        with self.app.app_context():
            db.create_all()

        self.app.run(debug=True) 
        
    def inicio(self):
        return render_template('forbicipeluqueria.html')

    def damas(self):
        return render_template('damas.html')

    def caballeros(self):
        return render_template('caballeros.html')

    def marcel_france(self):
        return render_template('marcelfrance.html')
    
    def reserva (self,servicio):
        
        if request.method=="POST":
            
            nombre=request.form['nombre']
            numero=request.form['numero']
            fecha=request.form['fecha']
            hora=request.form['hora']
            email=request.form['email']
            miReserva = Reservas(nombre,numero,fecha,hora,servicio,email)
            
            db.session.add(miReserva)
            db.session.commit()
            
            return redirect(url_for('inicio'))
        
        return render_template ('reserva.html')
    
    def reserva_producto (self,producto):
        
        if request.method=="POST":
            
            nombre=request.form['nombre']
            numero=request.form['numero']
            email=request.form['email']
            miReserva_productos = Reserva_Productos(nombre,numero,producto,email)
            
            db.session.add(miReserva_productos)
            db.session.commit()
            
            return redirect(url_for('inicio'))
        
        return render_template ('reservaproductos.html')
        
miPeluqueria = Forbici()
        