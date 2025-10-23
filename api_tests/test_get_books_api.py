import requests

BASE_URL = "https://bookstore.toolsqa.com"

def test_get_all_books():
    response = requests.get(f"{BASE_URL}/BookStore/v1/Books")
    assert response.status_code == 200, "Failed to fetch book list"
    data = response.json()
    assert "books" in data, "Books key missing"
    assert isinstance(data["books"], list), "Books should be a list"
    assert len(data["books"]) > 0, "No books found"
    assert response.elapsed.total_seconds() < 3
