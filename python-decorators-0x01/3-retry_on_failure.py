import time
import sqlite3 
import functools


#### paste your with_db_decorator here

def with_db_connection(func):
    """ your code goes here"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def retry_on_failure(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attemp in range(1, retries+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("An error occur")
                    if attemp == retries:
                        print("Max retries reached. Giving up.")
                        print(e)
                    else:
                        print("Delaying for {}".format(delay))
                        time.sleep(delay)
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT *s FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)