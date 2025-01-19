from flask import Blueprint, request, jsonify
from models.ruta import Ruta
from models.conductor import Conductor
from models import db

ruta_bp = Blueprint("rutas", __name__)

# Crear una nueva ruta
@ruta_bp.route("/", methods=["POST"])
def create_ruta():
    data = request.get_json()
    if not data or not all(k in data for k in ("notas", "fecha_programada", "conductor_id")):
        return jsonify({"error": "Los campos 'notas', 'fecha_programada' y 'conductor_id' son obligatorios"}), 400

    conductor = Conductor.query.get(data["conductor_id"])
    if not conductor:
        return jsonify({"error": "Conductor no encontrado"}), 404

    nueva_ruta = Ruta(
        notas=data["notas"],
        fecha_programada=data["fecha_programada"],
        conductor_id=data["conductor_id"]
    )
    db.session.add(nueva_ruta)
    db.session.commit()
    return jsonify({
        "id": nueva_ruta.id,
        "notas": nueva_ruta.notas,
        "fecha_programada": str(nueva_ruta.fecha_programada),
        "conductor_id": nueva_ruta.conductor_id
    }), 201

# Obtener todas las rutas
@ruta_bp.route("/", methods=["GET"])
def get_rutas():
    rutas = Ruta.query.all()
    resultado = [
        {
            "id": r.id,
            "notas": r.notas,
            "fecha_programada": str(r.fecha_programada),
            "conductor": r.conductor.nombre
        } for r in rutas
    ]
    return jsonify(resultado), 200

# Obtener una ruta por ID
@ruta_bp.route("/<int:id>", methods=["GET"])
def get_ruta(id):
    ruta = Ruta.query.get(id)
    if not ruta:
        return jsonify({"error": "Ruta no encontrada"}), 404
    return jsonify({
        "id": ruta.id,
        "notas": ruta.notas,
        "fecha_programada": str(ruta.fecha_programada),
        "conductor": ruta.conductor.nombre
    }), 200

# Editar una ruta
@ruta_bp.route("/<int:id>", methods=["PUT"])
def update_ruta(id):
    data = request.get_json()
    ruta = Ruta.query.get(id)
    if not ruta:
        return jsonify({"error": "Ruta no encontrada"}), 404

    # Validar los campos antes de actualizar
    if "notas" in data:
        ruta.notas = data["notas"]
    if "fecha_programada" in data:
        ruta.fecha_programada = data["fecha_programada"]
    if "conductor" in data:
        conductor = Conductor.query.get(data["conductor"])
        if not conductor:
            return jsonify({"error": "Conductor no encontrado"}), 404
        ruta.conductor_id = data["conductor"]

    db.session.commit()
    return jsonify({
        "id": ruta.id,
        "notas": ruta.notas,
        "fecha_programada": str(ruta.fecha_programada),
        "conductor": ruta.conductor.nombre
    }), 200

# Eliminar una ruta
@ruta_bp.route("/<int:id>", methods=["DELETE"])
def delete_ruta(id):
    ruta = Ruta.query.get(id)
    if not ruta:
        return jsonify({"error": "Ruta no encontrada"}), 404

    db.session.delete(ruta)
    db.session.commit()
    return jsonify({"message": "Ruta eliminada correctamente"}), 200

# Obtener las órdenes asociadas a una ruta
@ruta_bp.route("/<int:id>/ordenes", methods=["GET"])
def get_ruta_con_ordenes(id):
    # Busca la ruta por su ID
    ruta = Ruta.query.get(id)
    if not ruta:
        return jsonify({"error": "Ruta no encontrada"}), 404

    # Construye la respuesta con las órdenes asociadas
    ordenes = [
        {"id": o.id, "ruta_id": o.ruta_id, "prioridad": o.prioridad, "valor": o.valor}
        for o in ruta.ordenes
    ]

    return jsonify({
        "id": ruta.id,
        "notas": ruta.notas,
        "fecha_programada": str(ruta.fecha_programada),
        "conductor": ruta.conductor.nombre,
        "ordenes": ordenes
    }), 200