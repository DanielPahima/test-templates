import pytest
from app import app

@pytest.fixture
def client():
    # מגדירים את סביבת העבודה לבדיקה
    with app.test_client() as client:
        yield client

def test_hello(client):
    # שולחים בקשה ל-root של היישום
    response = client.get('/')
    
    # בודקים שהסטטוס קוד הוא 200 (OK)
    assert response.status_code == 200
    
    # בודקים שהתגובה מכילה את הטקסט "Hello, World!"
    assert response.data.decode('utf-8') == "Hello, World!"
