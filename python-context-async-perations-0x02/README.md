# 📘 Context Managers and Asynchronous Programming in Python

This project demonstrates advanced Python techniques for managing database connections and executing queries efficiently using **custom context managers** and **asynchronous programming**. It focuses on building reusable, safe, and performant patterns when working with SQLite in both synchronous and asynchronous environments.

---

## 🚀 Learning Objectives

By completing this project, you will:

- Understand and implement custom class-based context managers using `__enter__()` and `__exit__()`.
- Build reusable, clean database access logic using context managers.
- Perform asynchronous database operations with `aiosqlite` and `asyncio.gather()`.
- Run multiple queries concurrently to optimize performance.

---

## 📁 Project Structure

alx-backend-python/  
└── python-context-async-perations-0x02/  
  ├── 0-databaseconnection.py  # Custom DatabaseConnection context manager  
  ├── 1-execute.py        # ExecuteQuery reusable context manager with parameters  
  ├── 3-concurrent.py       # Asynchronous concurrent database queries  
  └── README.md         # Project documentation  

---

## ✅ Tasks Overview

### Task 0: Custom Class-Based Context Manager  
**File:** `0-databaseconnection.py`

- Create a class `DatabaseConnection` implementing `__enter__()` and `__exit__()`.
- Use `with DatabaseConnection()` to open and close a connection automatically.
- Execute a query to select all users: `SELECT * FROM users`.

---

### Task 1: Reusable Query Context Manager  
**File:** `1-execute.py`

- Implement `ExecuteQuery(query, params)` context manager class.
- It should open a connection, run the parameterized query (e.g., `age > 25`), and return results.
- Ensures clean execution using `__enter__()` and `__exit__()` methods.

---

### Task 2: Concurrent Asynchronous Database Queries  
**File:** `3-concurrent.py`

- Use `aiosqlite` to access SQLite asynchronously.
- Create two `async` functions:
  - `async_fetch_users()` — fetch all users.
  - `async_fetch_older_users()` — fetch users older than 40.
- Use `asyncio.gather()` to run both functions concurrently.
- Run with `asyncio.run(fetch_concurrently())`.

---

## 📦 Requirements

- Python 3.8 or higher  
- `aiosqlite` library → install with:  
  ```bash
  pip install aiosqlite
