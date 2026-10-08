import pytest
from fastapi.testclient import TestClient
from app.main import app, health_status
client=TestClient(app)
def test_v2_thermal_shape():
    body=client.get('/api/thermal').json(); assert body=={'Sensor':'CPU1','ReadingCelsius':72.0,'Health':'OK'}; assert 'TempC' not in body
@pytest.mark.parametrize('celsius,expected',[(74.9,'OK'),(75.0,'Warning'),(84.9,'Warning'),(85.0,'Critical')])
def test_health_boundaries(celsius,expected): assert health_status(celsius)==expected
