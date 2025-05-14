#!/usr/bin/python3
""""2-lazy_paginate - Function to simulte
fetching paginated data from the users database
using a generator to lazily load each page
"""

seed = __import__('seed')


def paginate_users(page_size, offset):
    """Fetch a single page of users from the database."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"""
                   SELECT * FROM user_data LIMIT
                   {page_size} OFFSET {offset}""")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """Generator that yields users one by one, loading pages lazily."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        for user in page:
            yield user
        offset += page_size
