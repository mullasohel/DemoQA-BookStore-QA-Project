import requests

BASE_URL = "https://bookstore.toolsqa.com"

def test_delete_user():
    token_resp = requests.post(
        f"{BASE_URL}/Account/v1/GenerateToken",
        json={"userName": "demoUser123", "password": "Demo@123"}
    )
    token = token_resp.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    user_id = "YOUR_USER_UUID_HERE"
    response = requests.delete(f"{BASE_URL}/Account/v1/User/{user_id}", headers=headers)
    assert response.status_code in [204, 400], "Unexpected delete user response"
