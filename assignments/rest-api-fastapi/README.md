# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using FastAPI, a high-performance Python web framework. You'll create a Book Library API that handles CRUD (Create, Read, Update, Delete) operations, implements data validation, and follows RESTful design principles.

## 📝 Tasks

### 🛠️ Setup and Basic GET Endpoint

#### Description
Set up your FastAPI project and create your first endpoint to retrieve all books from the library.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn using `pip install fastapi uvicorn`
- Create a `main.py` file with a FastAPI application instance
- Define a Book model with fields: id, title, author, year, and genre
- Create a GET endpoint at `/api/books` that returns a list of all books
- Include at least 3 sample books in your initial data
- Test the endpoint by running the server with `uvicorn main:app --reload`

### 🛠️ GET Single Book by ID

#### Description
Implement an endpoint to retrieve a specific book by its unique ID.

#### Requirements
Completed program should:

- Create a GET endpoint at `/api/books/{book_id}` that accepts a book ID as a path parameter
- Return the book data if found
- Return a 404 status code with an appropriate error message if the book is not found
- Use FastAPI's `HTTPException` for error handling
- Test with valid and invalid book IDs

### 🛠️ POST Endpoint to Add New Books

#### Description
Create an endpoint that allows users to add new books to the library.

#### Requirements
Completed program should:

- Create a POST endpoint at `/api/books` that accepts book data in the request body
- Use Pydantic models for request validation (title, author, year, genre)
- Automatically generate a unique ID for each new book
- Add the new book to your data storage
- Return the created book with a 201 status code
- Validate that all required fields are provided

### 🛠️ PUT and DELETE Endpoints

#### Description
Implement endpoints to update existing books and remove books from the library.

#### Requirements
Completed program should:

- Create a PUT endpoint at `/api/books/{book_id}` to update a book's information
- Create a DELETE endpoint at `/api/books/{book_id}` to remove a book
- Return appropriate status codes (200 for successful update/delete, 404 if not found)
- For PUT: validate the updated data using Pydantic models
- For DELETE: return a confirmation message
- Test all CRUD operations together

### 🛠️ (Bonus) Advanced Features

#### Description
Enhance your API with additional features to make it more robust and user-friendly.

#### Requirements
Enhanced version could include:

- Query parameters for filtering books by author or genre (e.g., `/api/books?author=Tolkien`)
- Search functionality to find books by partial title match
- Pagination for the book list (limit and offset parameters)
- API documentation using FastAPI's automatic Swagger UI (available at `/docs`)
- Input validation for year (must be between 1000 and current year)
- CORS middleware to allow frontend applications to access the API

