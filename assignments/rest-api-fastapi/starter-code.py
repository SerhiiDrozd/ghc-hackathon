"""
Starter Code for REST API with FastAPI Assignment
Book Library API - Complete the TODOs to build your REST API
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(title="Book Library API", version="1.0.0")

# TODO: Define your Book model using Pydantic BaseModel
# Include fields: id (int), title (str), author (str), year (int), genre (str)
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    genre: str


# TODO: Define a BookCreate model (without id field) for POST requests
class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: str


# Sample data - In-memory storage (list of dictionaries)
books_db = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy"},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction"},
]


# TODO: Task 1 - Create a GET endpoint to retrieve all books
# Endpoint: /api/books
# Should return: List of all books
@app.get("/api/books", response_model=List[Book])
def get_all_books():
    pass  # Replace with your code


# TODO: Task 2 - Create a GET endpoint to retrieve a single book by ID
# Endpoint: /api/books/{book_id}
# Should return: Book if found, 404 error if not found
@app.get("/api/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    pass  # Replace with your code


# TODO: Task 3 - Create a POST endpoint to add a new book
# Endpoint: /api/books
# Should accept: BookCreate model in request body
# Should return: Created book with generated ID, status code 201
@app.post("/api/books", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    pass  # Replace with your code


# TODO: Task 4 - Create a PUT endpoint to update a book
# Endpoint: /api/books/{book_id}
# Should accept: BookCreate model in request body
# Should return: Updated book if found, 404 error if not found
@app.put("/api/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    pass  # Replace with your code


# TODO: Task 5 - Create a DELETE endpoint to remove a book
# Endpoint: /api/books/{book_id}
# Should return: Success message if deleted, 404 error if not found
@app.delete("/api/books/{book_id}")
def delete_book(book_id: int):
    pass  # Replace with your code


# Root endpoint for testing
@app.get("/")
def root():
    return {"message": "Welcome to the Book Library API! Visit /docs for API documentation."}


# BONUS: Add query parameters for filtering
# BONUS: Add search functionality
# BONUS: Add pagination

"""
To run this application:
1. Install dependencies: pip install fastapi uvicorn
2. Run the server: uvicorn main:app --reload
3. Visit http://localhost:8000/docs to see the interactive API documentation
4. Test your endpoints using the Swagger UI or tools like Postman/curl
"""

