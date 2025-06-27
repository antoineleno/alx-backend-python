# 🧪 Unittests and Integration Tests in Python

This project focuses on mastering the concepts and implementation of **unit testing**, **integration testing**, **mocking**, **parameterization**, and **memoization** using Python's `unittest` framework, `unittest.mock`, and `parameterized`.

It’s part of the **ProDev Backend** track at ALX and aligns with best practices in testing modern Python codebases.

---

## 🚀 Learning Objectives

By completing this project, you will:

- Understand the **difference between unit and integration tests**.
- Use `unittest` to test individual Python functions and components.
- Apply **mocking techniques** to isolate and control dependencies.
- Leverage **parameterized tests** for broad coverage with minimal code.
- Write and structure tests using **fixtures** and **patching**.
- Use `memoization` to cache function results and test behavior with mocks.
- Run tests with `python -m unittest`.

---

## 📁 Project Structure

```bash
alx-backend-python/
└── 0x03-Unittests_and_integration_tests/
    ├── client.py                 # GithubOrgClient class (real-world API integration)
    ├── fixtures.py               # Test fixtures for integration tests
    ├── test_client.py           # Unit and integration tests for GithubOrgClient
    ├── test_utils.py            # Unit tests for utility functions (access_nested_map, get_json, memoize)
    ├── utils.py                  # Utility functions used across the project
    └── README.md                 # Project documentation
