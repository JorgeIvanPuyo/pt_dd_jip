from models import db
from models.conductor import Conductor
from models.ruta import Ruta
from models.orden import Orden
from datetime import date, timedelta
import os

def check_if_db_populated():
    """Verifica si la base de datos ya está poblada."""
    return Conductor.query.first() is not None

def populate_db():
    """Puebla la base de datos con datos iniciales."""
    # Crear conductores
    conductores = [
        Conductor(id=9, nombre="Eduardo B."),
        Conductor(id=10, nombre="José N."),
        Conductor(id=11, nombre="Mauricio J."),
        Conductor(id=12, nombre="Miguel T."),
        Conductor(id=13, nombre="Álvaro T."),
        Conductor(id=14, nombre="Juan D."),
        Conductor(id=15, nombre="Ariel F."),
        Conductor(id=16, nombre="Carlos M."),
        Conductor(id=17, nombre="Roberto R."),
        Conductor(id=18, nombre="Basilio M."),
        Conductor(id=19, nombre="Jorge G."),
        Conductor(id=20, nombre="Felipe V.")
    ]
    db.session.add_all(conductores)
    db.session.commit()

    # Crear rutas
    rutas = []
    for i in range(10):
        ruta = Ruta(
            id=i + 1000, 
            notas=f"Ruta de ejemplo {i + 1}",
            fecha_programada=date.today() + timedelta(days=i),
            conductor_id=conductores[i % len(conductores)].id
        )
        rutas.append(ruta)
    db.session.add_all(rutas)
    db.session.commit()

    # Crear órdenes
    ordenes = []
    for i in range(10):
        orden = Orden(
            id=i + 2000,  
            ruta_id=rutas[i % len(rutas)].id,
            prioridad=i % 2 == 0,
            valor=round(50 + i * 10.5, 2)
        )
        ordenes.append(orden)
    db.session.add_all(ordenes)
    db.session.commit()

def main():
    """Puebla la base de datos si no está poblada."""
    from src.main import app
    with app.app_context():
        if check_if_db_populated():
            print("La base de datos ya está poblada. No se realizarán cambios.")
        else:
            print("Poblando la base de datos...")
            populate_db()
            print("Base de datos poblada correctamente.")

if __name__ == "__main__":
    main()
