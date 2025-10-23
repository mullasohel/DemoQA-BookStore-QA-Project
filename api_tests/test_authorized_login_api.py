import requests

BASE_URL = "https://bookstore.toolsqa.com"
LOGIN_URL = f"{BASE_URL}/Account/v1/Authorized"

def test_authorized_login():
    payload = {
        "userName": "demoUser123",
        "password": "Demo@123"
    }
    response = requests.post(LOGIN_URL, json=payload)
    assert response.status_code == 200, "Login request failed"
    assert response.text.lower() in ["true", "false"], "Invalid response type"
