#!/usr/bin/python3
""""0-stream_users.py: Generator
that streams rows from an SQL database one by one.
"""
seed = __import__('seed')


def stream_users():
    """Function that uses a generator to fetch rows one
    by one from the user_data table. You must use the Yield python generator
    """
    connector = seed.connect_to_prodev()
    cursor = connector.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
    connector.close()
