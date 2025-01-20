from flask import Blueprint, request, jsonify
from models.ruta import Ruta
from models.conductor import Conductor
from models.orden import Orden
from models import db

ruta_bp = Blueprint("rutas", __name__)

# Crear una nueva ruta
@ruta_bp.route("/", methods=["POST"])
def create_ruta():
    data = request.get_json()
    if not data or not all(k in data for k in ("notas", "fecha_programada", "conductor")):
        return jsonify({"error": "Los campos 'notas', 'fecha_programada' y 'conductor' son obligatorios"}), 400

    # Validar que el campo conductor contenga el ID
    conductor_id = data["conductor"].get("id") if isinstance(data["conductor"], dict) else data["conductor"]
    conductor = Conductor.query.get(conductor_id)
    if not conductor:
        return jsonify({"error": "Conductor no encontrado"}), 404

    # Validar que la ruta con el ID no exista
    if "id" in data and Ruta.query.get(data["id"]):
        return jsonify({"error": f"La ruta con ID {data['id']} ya existe"}), 400

    # Crear la nueva ruta
    nueva_ruta = Ruta(
        id=data.get("id"),  
        notas=data["notas"],
        fecha_programada=data["fecha_programada"],
        conductor_id=conductor_id
    )

    # Agregar la nueva ruta a la base de datos
    db.session.add(nueva_ruta)
    db.session.commit()

    # Crear las órdenes asociadas si existen en la data
    if "ordenes" in data:
        for orden_data in data["ordenes"]:
            nueva_orden = Orden(
                id=orden_data.get("id"),  # Respetar el ID si viene especificado
                ruta_id=nueva_ruta.id,
                prioridad=orden_data.get("prioridad", False),
                valor=orden_data.get("valor", 0.0)
            )
            db.session.add(nueva_orden)

    # Confirmar todas las transacciones
    db.session.commit()

    return jsonify({
        "id": nueva_ruta.id,
        "notas": nueva_ruta.notas,
        "fecha_programada": str(nueva_ruta.fecha_programada),
        "conductor": {
            "id": conductor.id,
            "nombre": conductor.nombre
        },
        "ordenes": [
            {
                "id": orden.id,
                "prioridad": orden.prioridad,
                "valor": orden.valor
            }
            for orden in nueva_ruta.ordenes
        ]
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

    # Validar y actualizar los campos de la ruta
    if "notas" in data:
        ruta.notas = data["notas"]
    if "fecha_programada" in data:
        ruta.fecha_programada = data["fecha_programada"]
    if "conductor" in data:
        # Validar que el conductor sea un objeto y extraer su id
        conductor_id = data["conductor"].get("id") if isinstance(data["conductor"], dict) else data["conductor"]
        conductor = Conductor.query.get(conductor_id)
        if not conductor:
            return jsonify({"error": "Conductor no encontrado"}), 404
        ruta.conductor_id = conductor_id

    # Actualizar órdenes asociadas
    if "ordenes" in data:
        for orden_data in data["ordenes"]:
            orden = next((o for o in ruta.ordenes if o.id == orden_data["id"]), None)
            if orden:
                # Actualizar los campos de la orden existente
                orden.prioridad = orden_data.get("prioridad", orden.prioridad)
                orden.valor = orden_data.get("valor", orden.valor)
            else:
                # Crear una nueva orden si no existe
                nueva_orden = Orden(
                    id=orden_data["id"],
                    ruta_id=ruta.id,
                    prioridad=orden_data.get("prioridad", False),
                    valor=orden_data.get("valor", 0),
                )
                db.session.add(nueva_orden)

    db.session.commit()

    return jsonify({
        "id": ruta.id,
        "notas": ruta.notas,
        "fecha_programada": str(ruta.fecha_programada),
        "conductor": {
            "id": ruta.conductor.id,
            "nombre": ruta.conductor.nombre
        },
        "ordenes": [
            {"id": o.id, "prioridad": o.prioridad, "valor": o.valor} for o in ruta.ordenes
        ]
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
        "conductor": {
            "id": ruta.conductor.id,
            "nombre": ruta.conductor.nombre
        },
        "ordenes": ordenes
    }), 200