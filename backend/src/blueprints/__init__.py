from flask import Blueprint
from .conductores import conductor_bp
from .rutas import ruta_bp
from .ordenes import orden_bp
from .utilidades import utilidades_bp
from .fetch_json_server import fetch_bp

def create_blueprints(app):
    app.register_blueprint(conductor_bp, url_prefix="/conductores")
    app.register_blueprint(ruta_bp, url_prefix="/rutas")
    app.register_blueprint(orden_bp, url_prefix="/ordenes")
    app.register_blueprint(utilidades_bp, url_prefix="/utilidades")
    app.register_blueprint(fetch_bp, url_prefix="/fetch")
