import pytest
from app.app import app  # ייבוא נכון של ה-Flask app מתוך תיקיית app

@pytest.fixture
def client():
    # יוצר client עבור Flask לצורך הבדיקות
    with app.test_client() as client:
        yield client

def test_hello(client):
    # שולח בקשה ל-root של היישום
    response = client.get('/')
    
    # בודק שהסטטוס קוד הוא 200 (OK)
    assert response.status_code == 200
    
    # בודק שהתגובה מכילה את הטקסט "Hello, World!"
    assert response.data.decode('utf-8') == "Hello, World!"
