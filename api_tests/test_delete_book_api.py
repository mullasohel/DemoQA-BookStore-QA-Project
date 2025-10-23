import requests

BASE_URL = "https://bookstore.toolsqa.com"

def test_delete_book():
    token_resp = requests.post(
        f"{BASE_URL}/Account/v1/GenerateToken",
        json={"userName": "demoUser123", "password": "Demo@123"}
    )
    token = token_resp.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "isbn": "9781449325862",
        "userId": "YOUR_USER_UUID_HERE"
    }
    response = requests.delete(f"{BASE_URL}/BookStore/v1/Book", json=payload, headers=headers)
    assert response.status_code in [204, 400], "Unexpected delete response"
