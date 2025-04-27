from app import app

def test_hello_world():
    response = app.test_client().get('/')  # Sends a GET request to the specified path
    assert response.status_code == 200
    assert response.data == b'Hello, World!'