from fastapi import FastAPI

app = FastAPI(
    title="Thống kê dữ liệu sách trong thư viện",
    description="Nguyen Huu Bao Lam",
    version="1.0.0"
)

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "status": "available_books"
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "status": "available_books"
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "status": "available_books"
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "status": "borrowed_books"
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "status": "borrowed_books"
    }
]


# 1. Thống kê số lượng sách
@app.get("/books/statistics")
def get_statistics():
    available = 0
    borrowed = 0

    for book in books:
        if book["status"] == "available_books":
            available += 1
        else:
            borrowed += 1

    return {
        "total_books": len(books),
        "available_books": available,
        "borrowed_books": borrowed
    }


# 2. Lấy danh sách thể loại
@app.get("/books/categories")
def get_categories():
    categories = []

    for book in books:
        if book["category"] not in categories:
            categories.append(book["category"])

    return {
        "categories": categories
    }


# 3. Lấy sách mới nhất
@app.get("/books/latest")
def get_latest():
    if len(books) == 0:
        return {
            "message": "No books available"
        }

    newest_book = books[0]

    for book in books:
        if book["year"] > newest_book["year"]:
            newest_book = book

    return newest_book