#!/usr/bin/python3
""""Python script that sets up a MySQL database and table,
    inserts CSV data into it, and defines a generator function
    to stream user data rows one by one from the databas
"""

import mysql.connector
from os import getenv
import uuid
import csv

# ----------- Function Definitions -----------


def connect_db():
    """connects to the mysql database server"""
    username = getenv("USERNAME")
    password = getenv("PASSWORD")
    try:
        connector = mysql.connector.connect(
            host='localhost',
            username=username,
            password=password
        )
        return connector
    except Exception as e:
        print("Error {}".format(e))
        return None


def create_database(connection):
    """creates the database ALX_prodev if it does not exist"""
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database 'ALX_prodev Sucessfully created")
    except Exception as e:
        print("Error {}".format(e))
    cursor.close()


def connect_to_prodev():
    """connects the the ALX_prodev database in MYSQL"""
    username = getenv("USERNAME")
    password = getenv("PASSWORD")
    try:
        connector = mysql.connector.connect(
            host='localhost',
            username=username,
            password=password,
            database='ALX_prodev'
        )
        return connector
    except Exception as e:
        print("Error {}".format(e))
        return None


def create_table(connection):
    """creates a table user_data if it does not exists
    with the required fields
    """
    cursor = connection.cursor()
    create_table_query = """CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(3, 0) NOT NULL,
        INDEX (user_id)
    )
       """
    try:
        cursor.execute(create_table_query)
        print("Table user_data successfully created")
    except Exception as e:
        print("Effor: {}".format(e))




def insert_data(connection, data):
    """inserts data in the database if it does not exist"""

    dataset = []
    check_query = "SELECT COUNT(*) FROM user_data WHERE email = %s"
    insert_query = """
    INSERT INTO user_data (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    """
    with open(data, newline='') as csvfile, connection.cursor() as cursor:
        reader = csv.DictReader(csvfile)
        dataset = (row for row in reader)
        for i in range(1000):
            row = next(dataset)
            cursor.execute(check_query, (row['email'],))
            exists = cursor.fetchone()[0]
            if exists == 0:
                uid = str(uuid.uuid4())
                cursor.execute(insert_query, (uid, row['name'], row['email'], row['age']))
            else:
                print(f"Skipped (already exists): {row['email']}")
    connection.commit()
