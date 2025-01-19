from . import db

class Ruta(db.Model):
    __tablename__ = 'rutas'

    id = db.Column(db.Integer, primary_key=True)
    notas = db.Column(db.String(500))
    fecha_programada = db.Column(db.Date, nullable=False)
    conductor_id = db.Column(db.Integer, db.ForeignKey('conductores.id'), nullable=False)

    conductor = db.relationship('Conductor', backref='rutas')
