import requests

BASE_URL = "https://bookstore.toolsqa.com"
CREATE_USER_URL = f"{BASE_URL}/Account/v1/User"

def test_create_user():
    payload = {
        "userName": "demoUser123",
        "password": "Demo@123"
    }
    response = requests.post(CREATE_USER_URL, json=payload)
    assert response.status_code == 201, f"Unexpected code: {response.status_code}"
    data = response.json()
    assert "userID" in data, "userID missing in response"
    assert data["username"] == "demoUser123", "Username mismatch"
    assert isinstance(data["books"], list), "Books should be list"
    assert response.elapsed.total_seconds() < 3
