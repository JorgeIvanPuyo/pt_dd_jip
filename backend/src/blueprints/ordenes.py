from flask import Blueprint, request, jsonify
from models.orden import Orden
from models.ruta import Ruta
from models import db

orden_bp = Blueprint("ordenes", __name__)

# Crear una nueva orden
@orden_bp.route("/", methods=["POST"])
def create_orden():
    data = request.get_json()
    if not data or not all(k in data for k in ("ruta_id", "prioridad")):
        return jsonify({"error": "Los campos 'ruta_id' y 'prioridad' son obligatorios"}), 400

    ruta = Ruta.query.get(data["ruta_id"])
    if not ruta:
        return jsonify({"error": "Ruta no encontrada"}), 404

    nueva_orden = Orden(
        ruta_id=data["ruta_id"],
        prioridad=data["prioridad"],
        valor=data["valor"]
    )
    db.session.add(nueva_orden)
    db.session.commit()
    return jsonify({
        "id": nueva_orden.id,
        "ruta_id": nueva_orden.ruta_id,
        "prioridad": nueva_orden.prioridad,
        "valor": nueva_orden.valor
    }), 201

# Obtener todas las órdenes
@orden_bp.route("/", methods=["GET"])
def get_ordenes():
    ordenes = Orden.query.all()
    resultado = [
        {
            "id": o.id,
            "ruta_id": o.ruta_id,
            "prioridad": o.prioridad,
            "valor": o.valor
        } for o in ordenes
    ]
    return jsonify(resultado), 200

# Obtener una orden por ID
@orden_bp.route("/<int:id>", methods=["GET"])
def get_orden(id):
    orden = Orden.query.get(id)
    if not orden:
        return jsonify({"error": "Orden no encontrada"}), 404
    return jsonify({
        "id": orden.id,
        "ruta_id": orden.ruta_id,
        "prioridad": orden.prioridad,
        "valor": orden.valor
    }), 200

# Editar una orden
@orden_bp.route("/<int:id>", methods=["PUT"])
def update_orden(id):
    data = request.get_json()
    orden = Orden.query.get(id)
    if not orden:
        return jsonify({"error": "Orden no encontrada"}), 404

    if "ruta_id" in data:
        ruta = Ruta.query.get(data["ruta_id"])
        if not ruta:
            return jsonify({"error": "Ruta no encontrada"}), 404
        orden.ruta_id = data["ruta_id"]

    if "prioridad" in data:
        orden.prioridad = data["prioridad"]

    if "valor" in data:  
        orden.valor = data["valor"]

    db.session.commit()
    return jsonify({
        "id": orden.id,
        "ruta_id": orden.ruta_id,
        "prioridad": orden.prioridad,
        "valor": orden.valor
    }), 200

# Eliminar una orden
@orden_bp.route("/<int:id>", methods=["DELETE"])
def delete_orden(id):
    orden = Orden.query.get(id)
    if not orden:
        return jsonify({"error": "Orden no encontrada"}), 404

    db.session.delete(orden)
    db.session.commit()
    return jsonify({"message": "Orden eliminada correctamente"}), 200
