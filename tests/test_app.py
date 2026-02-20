import pytest
from app import app

@pytest.fixture
def client():
    # Create a test client using the Flask app configuration
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the Root Endpoint returns 200 and correct JSON"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"DevSecOps" in response.data

def test_health_route(client):
    """Test the Health Endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'up'