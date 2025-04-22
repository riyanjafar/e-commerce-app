import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_anasayfa(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Hızlı Telefon' in response.data.decode('utf-8') 

def test_sepete_ekle(client):
    response = client.get('/ekle/1')
    assert response.status_code == 302 
    
    response = client.get('/sepet')
    assert response.status_code == 200
    assert 'Hızlı Telefon' in response.data.decode('utf-8') 
