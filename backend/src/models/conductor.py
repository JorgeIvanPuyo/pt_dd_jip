from . import db

class Conductor(db.Model):
    __tablename__ = "conductores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)

    # Relación con rutas
    rutas = db.relationship("Ruta", back_populates="conductor")

    def __init__(self, nombre, id=None):
        self.nombre = nombre
        if id is not None:
            self.id = id