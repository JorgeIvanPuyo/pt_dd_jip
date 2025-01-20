from flask import Blueprint, jsonify
from models import db
from models.conductor import Conductor
from models.ruta import Ruta
from models.orden import Orden
from datetime import date, timedelta
import random

utilidades_bp = Blueprint("utilidades", __name__)

@utilidades_bp.route("/poblar", methods=["POST"])
def poblar_base_datos():
    try:
        # Crear 12 conductores
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

        # Crear 5 rutas con IDs definidos o autogenerados
        rutas = []
        for i in range(5):
            ruta = Ruta(
                id=i + 1000,  # Asignar IDs específicos (opcional)
                notas=f"Ruta de ejemplo {i + 1}",
                fecha_programada=date.today() + timedelta(days=i),
                conductor_id=random.choice([c.id for c in conductores])
            )
            rutas.append(ruta)
        db.session.add_all(rutas)
        db.session.commit()

        # Crear 5 órdenes vinculadas a las rutas
        ordenes = []
        for i in range(5):
            orden = Orden(
                id=i + 2000,  # Asignar IDs específicos (opcional)
                ruta_id=random.choice([r.id for r in rutas]),
                prioridad=random.choice([True, False]),
                valor=round(random.uniform(50, 500), 2)
            )
            ordenes.append(orden)
        db.session.add_all(ordenes)
        db.session.commit()

        return jsonify({
            "message": "Base de datos poblada con éxito",
            "conductores": len(conductores),
            "rutas": len(rutas),
            "ordenes": len(ordenes)
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
