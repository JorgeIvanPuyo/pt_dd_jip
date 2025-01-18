from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo de Conductores
class Conductor(db.Model):
    __tablename__ = 'conductores'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)

    # Relación con Rutas
    rutas = db.relationship('Ruta', back_populates='conductor', cascade='all, delete-orphan')

# Modelo de Rutas
class Ruta(db.Model):
    __tablename__ = 'rutas'

    id = db.Column(db.Integer, primary_key=True)
    notas = db.Column(db.String(500))
    fecha_programada = db.Column(db.Date, nullable=False)
    conductor_id = db.Column(db.Integer, db.ForeignKey('conductores.id'), nullable=False)

    # Relación con Conductores
    conductor = db.relationship('Conductor', back_populates='rutas')

    # Relación con Órdenes
    ordenes = db.relationship('Orden', back_populates='ruta', cascade='all, delete-orphan')

# Modelo de Órdenes
class Orden(db.Model):
    __tablename__ = 'ordenes'

    id = db.Column(db.Integer, primary_key=True)
    ruta_id = db.Column(db.Integer, db.ForeignKey('rutas.id'), nullable=False)
    prioridad = db.Column(db.Boolean, default=False)

    # Relación con Rutas
    ruta = db.relationship('Ruta', back_populates='ordenes')