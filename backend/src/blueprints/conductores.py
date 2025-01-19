from flask import Blueprint, request, jsonify
from models.conductor import Conductor
from models import db

conductor_bp = Blueprint("conductores", __name__)

# Crear un nuevo conductor
@conductor_bp.route("/", methods=["POST"])
def create_conductor():
    data = request.get_json()
    if not data or not data.get("nombre"):
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    
    if "id" in data and Conductor.query.get(data["id"]):
        return jsonify({"error": f"El ID {data['id']} ya existe en la base de datos"}), 400

    nuevo_conductor = Conductor(
        id=data.get("id"),  
        nombre=data["nombre"]
    )
    db.session.add(nuevo_conductor)
    db.session.commit()
    return jsonify({"id": nuevo_conductor.id, "nombre": nuevo_conductor.nombre}), 201

# Obtener todos los conductores
@conductor_bp.route("/", methods=["GET"])
def get_conductores():
    conductores = Conductor.query.all()
    resultado = [{"id": c.id, "nombre": c.nombre} for c in conductores]
    return jsonify(resultado), 200

# Obtener un conductor por ID
@conductor_bp.route("/<int:id>", methods=["GET"])
def get_conductor(id):
    conductor = Conductor.query.get(id)
    if not conductor:
        return jsonify({"error": "Conductor no encontrado"}), 404
    return jsonify({"id": conductor.id, "nombre": conductor.nombre}), 200

# Editar un conductor
@conductor_bp.route("/<int:id>", methods=["PUT"])
def update_conductor(id):
    data = request.get_json()
    conductor = Conductor.query.get(id)
    if not conductor:
        return jsonify({"error": "Conductor no encontrado"}), 404

    if "nombre" in data:
        conductor.nombre = data["nombre"]

    db.session.commit()
    return jsonify({"id": conductor.id, "nombre": conductor.nombre}), 200

# Eliminar un conductor
@conductor_bp.route("/<int:id>", methods=["DELETE"])
def delete_conductor(id):
    conductor = Conductor.query.get(id)
    if not conductor:
        return jsonify({"error": "Conductor no encontrado"}), 404

    db.session.delete(conductor)
    db.session.commit()
    return jsonify({"message": "Conductor eliminado correctamente"}), 200
