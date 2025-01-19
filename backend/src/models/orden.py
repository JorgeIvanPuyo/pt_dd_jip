from . import db

class Orden(db.Model):
    __tablename__ = 'ordenes'

    id = db.Column(db.Integer, primary_key=True)
    ruta_id = db.Column(db.Integer, db.ForeignKey('rutas.id'), nullable=False)
    prioridad = db.Column(db.Boolean, default=False)
    valor = db.Column(db.Float, nullable=False)

    ruta = db.relationship('Ruta', backref='ordenes')