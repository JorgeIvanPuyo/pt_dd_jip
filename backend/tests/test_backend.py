import pytest

def test_create_ruta_missing_fields(client):
    payload = {
        "fecha_programada": "2025-01-25"
    }

    response = client.post('/rutas/', json=payload)

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Los campos 'notas', 'fecha_programada' y 'conductor' son obligatorios"
    }

def test_create_ruta_missing_conductor(client):
    payload = {
        "notas": "Ruta sin conductor",
        "fecha_programada": "2025-01-25",
    }

    response = client.post('/rutas/', json=payload)

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Los campos 'notas', 'fecha_programada' y 'conductor' son obligatorios"
    }

def test_create_ruta_valid_data(client):
    payload = {
        "id": 1,
        "notas": "Ruta válida",
        "fecha_programada": "2025-01-25",
        "conductor": {"id": 9}  
    }

    response = client.post('/rutas/', json=payload)

    assert response.status_code == 201
    assert "id" in response.get_json() 

def test_create_ruta_duplicate_id(client):
    payload = {
        "id": 1,  
        "notas": "Ruta duplicada",
        "fecha_programada": "2025-01-25",
        "conductor": {"id": 9}
    }

    response = client.post('/rutas/', json=payload)
    
    assert response.status_code == 400
    assert response.get_json() == {"error": "La ruta con ID 1000 ya existe"}

def test_delete_route_no_exist(client):
    response = client.delete('/rutas/3')
    assert response.status_code == 404
    assert response.get_json() == {"error": "Ruta no encontrada"}

def test_delete_route(client):
    response = client.delete('/rutas/1')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Ruta eliminada correctamente"}