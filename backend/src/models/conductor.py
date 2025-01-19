from . import db

class Conductor(db.Model):
    __tablename__ = 'conductores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre, id=None):
        self.nombre = nombre
        if id is not None: 
            self.id = id