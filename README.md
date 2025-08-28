# Stack
- Python 3.11.9
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn

# Features
- Create a new user
- Get all users
- Get user by ID
- Update user data
- Delete user

# How to launch
1. Clone the repository
2. Create activate a venv
3. Install dependencies from requirements.txt
4. Set up a database and update db URL in .env file to your data in PostgreSQL
5. Run the server by the command:
     ```uvicorn app.main:app --reload```
6. Open API docs to test endpoints:
    Swagger UI: http://127.0.0.1:8000/docs
    Redoc: http://127.0.0.1:8000/redoc
