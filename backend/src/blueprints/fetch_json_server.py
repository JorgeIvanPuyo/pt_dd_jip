from flask import Blueprint, request, jsonify
from models.ruta import Ruta
from models.conductor import Conductor
from models import db
import requests
from datetime import datetime

fetch_bp = Blueprint("fetch", __name__)

# Configuración del JSON Server
JSON_SERVER_URL = "http://json-server:3001/routes"

@fetch_bp.route("/<int:id>", methods=["GET"])
def fetch_route(id):
    # Intentar obtener la ruta desde la base de datos
    ruta = Ruta.query.get(id)
    if ruta:
        
        # Retornar la ruta encontrada en la base de datos
        return jsonify({
            "id": ruta.id,
            "notas": ruta.notas,
            "fecha_programada": str(ruta.fecha_programada),
            "conductor": {
                "id": ruta.conductor.id,
                "nombre": ruta.conductor.nombre
            },
            "ordenes": [
                {"id": o.id, "prioridad": o.prioridad, "valor": o.valor}
                for o in ruta.ordenes
            ],
            "source": "db"
        }), 200

    # Si no se encuentra en la base de datos, consultar al JSON Server
    try:
        response = requests.get(f"{JSON_SERVER_URL}/{id}")
        if response.status_code == 200:
            # Procesar la respuesta del JSON Server
            json_data = response.json()

            # Verificar si el conductor existe en la base de datos
            conductor_id = json_data.get("driverId")
            conductor = Conductor.query.get(conductor_id)

            # Completar la información del conductor
            formatted_data = {
                "id": int(json_data["id"]),
                "notas": json_data.get("notes"),
                "fecha_programada": datetime.fromisoformat(json_data["date"]).strftime("%Y-%m-%d")
                if json_data.get("date") else None,
                "conductor": {
                    "id": conductor_id,
                    "nombre": conductor.nombre if conductor else None
                },
                "ordenes": [
                    {
                        "id": orden["id"],
                        "prioridad": orden["priority"],
                        "valor": orden["value"]
                    }
                    for orden in json_data.get("orders", [])
                ]
            }
            formatted_data["source"] = "external"
            # Retornar los datos formateados
            return jsonify(formatted_data), 200
        else:
            return jsonify({"error": "Ruta no encontrada en la base de datos ni en el servicio externo"}), 404
    except requests.RequestException as e:
        # Manejo de errores en la comunicación con el JSON Server
        return jsonify({"error": "Error al comunicarse con el JSON Server", "details": str(e)}), 500
