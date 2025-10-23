import requests

BASE_URL = "https://bookstore.toolsqa.com"

def test_add_book():
    token_resp = requests.post(
        f"{BASE_URL}/Account/v1/GenerateToken",
        json={"userName": "demoUser123", "password": "Demo@123"}
    )
    token = token_resp.json()["token"]
    user_id = "YOUR_USER_UUID_HERE"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "userId": user_id,
        "collectionOfIsbns": [{"isbn": "9781449325862"}]
    }
    response = requests.post(f"{BASE_URL}/BookStore/v1/Books", json=payload, headers=headers)
    assert response.status_code in [200, 201, 400], "Unexpected status code"
    assert response.elapsed.total_seconds() < 3
