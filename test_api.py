import json
from fastapi.testclient import TestClient
from main import app
import unittest




client = TestClient(app)


### Testing whit pytest
def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Testing endpoint root": "Integracion y entrega continua de software"}

def test_url():
    response = client.get("/weather")
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data is not None
    assert len(data) > 0

def error_cases():
    response = client.post("/weather")
    assert response.status_code == 405
    assert response.json()['detail'] == "Method not allowed motherfoca"



### Testing with unittest
class TestWeatherEndpoint(unittest.TestCase):
    def test_invalid_url(self):
        response = client.get("/weather?url=invalid")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Invalid URL, does not comply with the protocol"})


