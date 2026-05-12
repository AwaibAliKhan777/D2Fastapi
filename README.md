# 🎓 Student Management API

A RESTful API built using FastAPI and SQLAlchemy to perform full CRUD operations on student data.
This project demonstrates backend development with database integration.

---

## 🚀 Features

* ➕ Create a new student
* 📄 Get all students
* 🔍 Get student by ID
* ✏️ Update student details
* ❌ Delete a student
* 🗄️ Database integration using SQLite

---

## 🛠️ Tech Stack

* Python 3.x
* FastAPI
* SQLAlchemy (ORM)
* SQLite (Database)
* Uvicorn (Server)
* Pydantic (Validation)

---

## 📂 Project Structure

```id="2o7u9y"
student-api/
│── main.py        # FastAPI app (routes + logic)
│── students.db    # SQLite database
│── README.md      # Documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone repository

```id="z6q1zq"
git clone https://github.com/your-username/student-api.git
cd student-api
```

### 2. Create virtual environment

```id="zjpv0i"
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```id="3ghw04"
pip install fastapi uvicorn sqlalchemy
```

### 4. Run server

```id="lfd70q"
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| POST   | /students      | Create student    |
| GET    | /students      | Get all students  |
| GET    | /students/{id} | Get student by ID |
| PUT    | /students/{id} | Update student    |
| DELETE | /students/{id} | Delete student    |

---

## 📥 Example Request (POST)

```json id="97hnr9"
{
  "name": "John Doe",
  "age": 21
}
```

---

## 📊 API Documentation

* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc

---

## 🧠 Concepts Covered

* CRUD operations
* REST API design
* Database connection
* SQLAlchemy ORM
* Models vs Schemas
* Dependency Injection (DB sessions)
* Error handling

---

## 🔮 Future Improvements

* Switch to PostgreSQL
* Add authentication (JWT)
* Pagination & filtering
* Docker deployment



---

## ⭐ Support

If you like this project, give it a star ⭐
