# 📘 DemoQA BookStore API Automation Suite

This project automates functional testing of the public **Book Store API** by ToolsQA.

### 🔗 Base URL
`https://bookstore.toolsqa.com`

## ✅ API Test Coverage

| Test File | Description |
|------------|--------------|
| test_create_user_api.py | Create a new user |
| test_login_api.py | Generate token for user |
| test_authorized_login_api.py | Verify user authorization |
| test_get_books_api.py | Get all books |
| test_get_book_by_isbn_api.py | Fetch single book details |
| test_add_book_api.py | Add book to user collection |
| test_delete_book_api.py | Delete a book from collection |
| test_delete_user_api.py | Delete a user |

### 🧪 Run Tests
```bash
pip install pytest requests
pytest api_tests/ --maxfail=1 --disable-warnings -v
```

### 📊 Validations
- Status code checks (200, 201, 204)
- JSON structure and keys
- Response time < 3 seconds

### 📸 Report
```bash
pytest api_tests/ --html=reports/report.html
```
