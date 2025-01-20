from . import db

class Ruta(db.Model):
    __tablename__ = "rutas"

    id = db.Column(db.Integer, primary_key=True)
    notas = db.Column(db.String(500), nullable=True)
    fecha_programada = db.Column(db.Date, nullable=False)
    conductor_id = db.Column(db.Integer, db.ForeignKey("conductores.id"), nullable=False)

    # Relación con conductores
    conductor = db.relationship("Conductor", back_populates="rutas")

    # Relación con órdenes
    ordenes = db.relationship("Orden", backref="ruta", cascade="all, delete-orphan")

    def __init__(self, notas, fecha_programada, conductor_id, id=None):
        self.notas = notas
        self.fecha_programada = fecha_programada
        self.conductor_id = conductor_id
        if id is not None:
            self.id = id
