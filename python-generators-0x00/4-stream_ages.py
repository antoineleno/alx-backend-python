#!/usr/bin/python3
""""4-stream_ages.py - Function taht use a generator
to compute a memory-efficient aggregate function
i.e average age for a large dataset
"""

seed = __import__('seed')


def stream_user_ages():
    """Generator that yields ages one by one from the database."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield age
    cursor.close()
    connection.close()


def calculate_average_age():
    """Calculate and print average age using streamed data."""
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1

    average = total_age / count if count > 0 else 0
    print(f"Average age of users: {average:.2f}")


calculate_average_age()
