# Python Generator-Based Data Streaming System

## About the Project

This project demonstrates the power and practicality of Python generators for building scalable, memory-efficient systems that interact with large SQL datasets. It provides a real-world simulation of streaming, batch processing, lazy pagination, and aggregation using generators to improve performance and resource usage in data-driven applications.

## Key Features

- **Database Initialization**: Automatically sets up a MySQL database (`ALX_prodev`) and seeds it with structured user data from a CSV file.
- **Row Streaming**: Implements generators to stream database records one by one without loading all data into memory.
- **Batch Processing**: Supports efficient batch-wise data processing for scalable analytics.
- **Lazy Pagination**: Simulates real-world paginated APIs by fetching data only when needed.
- **Efficient Aggregation**: Calculates metrics like average age without storing the entire dataset in memory.

## Technologies Used

- Python 3.x
- MySQL
- CSV and SQL standard libraries
- UUID for unique user IDs
- Git & GitHub for version control

## Learning Outcomes

- Mastered Python generators for iterative and on-demand data processing.
- Implemented lazy loading and pagination techniques.
- Integrated Python with MySQL to build a robust backend data pipeline.
- Achieved performance optimization by minimizing memory footprint in data operations.

## Getting Started

1. Ensure MySQL is installed and running locally.
2. Set environment variables for `USERNAME` and `PASSWORD`.
3. Run `seed.py` to set up the database and insert data.
4. Use the scripts to stream, process, and analyze the data as required.

## Repository Structure

