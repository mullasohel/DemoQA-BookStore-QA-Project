import requests

BASE_URL = "https://bookstore.toolsqa.com"
LOGIN_URL = f"{BASE_URL}/Account/v1/GenerateToken"

def test_generate_token():
    payload = {
        "userName": "demoUser123",
        "password": "Demo@123"
    }
    response = requests.post(LOGIN_URL, json=payload)
    assert response.status_code == 200, "Token generation failed"
    data = response.json()
    assert "token" in data, "Token key missing"
    assert data["status"] == "Success"
    assert response.elapsed.total_seconds() < 2
