# Python Decorators for Database Operations

## Overview
This project is part of the **ProDev Backend** curriculum and focuses on leveraging **Python decorators** to streamline and enhance database operations. By completing these tasks, developers gain hands-on experience with advanced Python features and best practices in managing database interactions efficiently.

## Key Objectives
- Master the use of **decorators** for modular, reusable code.
- Automate **logging**, **connection management**, **transactions**, **retry logic**, and **caching** in database workflows.
- Build robust, clean, and scalable Python applications interacting with databases.

## Project Requirements
- Python 3.8 or higher
- SQLite3 with a preconfigured `users` table
- Git and GitHub for version control
- Working knowledge of Python decorators and SQL basics

## Features & Tasks

### ✅ Task 0: Log Database Queries
Create `@log_queries` to log every SQL query executed, improving transparency and observability.

### ✅ Task 1: Manage Database Connections
Implement `@with_db_connection` to handle database opening and closing automatically, reducing boilerplate.

### ✅ Task 2: Transaction Management
Build `@transactional` to ensure atomic database transactions with proper commit/rollback.

### ✅ Task 3: Retry on Failure
Use `@retry_on_failure(retries=3, delay=1)` to automatically retry failed queries due to transient issues.

### ✅ Task 4: Cache Query Results
Design `@cache_query` to cache database query results and avoid redundant executions.

## Directory Structure

```text
alx-backend-python/
└── python-decorators-0x01/
    ├── 0-log_queries.py
    ├── 1-with_db_connection.py
    ├── 2-transactional.py
    ├── 3-retry_on_failure.py
    ├── 4-cache_query.py
    └── README.md
