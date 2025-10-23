import requests

BASE_URL = "https://bookstore.toolsqa.com"

def test_get_book_by_isbn():
    isbn = "9781449325862"
    response = requests.get(f"{BASE_URL}/BookStore/v1/Book?ISBN={isbn}")
    assert response.status_code == 200, "Failed to fetch book details"
    data = response.json()
    assert data["isbn"] == isbn, "ISBN mismatch"
    assert "title" in data and "author" in data, "Book data incomplete"
    assert isinstance(data["pages"], int), "Invalid pages data type"
    assert response.elapsed.total_seconds() < 2
