from . import db

class Orden(db.Model):
    __tablename__ = 'ordenes'

    id = db.Column(db.Integer, primary_key=True)
    ruta_id = db.Column(db.Integer, db.ForeignKey('rutas.id'), nullable=False)
    prioridad = db.Column(db.Boolean, default=False, nullable=True)
    valor = db.Column(db.Float, nullable=False)

    def __init__(self, ruta_id, prioridad=False, valor=0.0, id=None):
        self.ruta_id = ruta_id
        self.prioridad = prioridad
        self.valor = valor
        if id is not None:
            self.id = id
