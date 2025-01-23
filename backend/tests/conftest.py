import pytest
from src.main import app

@pytest.fixture
def client():
    """Fixture para configurar el cliente de prueba con contexto de aplicación."""
    app.config['TESTING'] = True 
    with app.app_context(): 
        with app.test_client() as client:
            yield client
