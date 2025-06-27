import sqlite3


class ExecuteQuery:
    def __init__(self, query, params=()):
        self.conn = None
        self.cursor = None
        self.result = None
        self.query = query
        self.params = params
    

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()



query = "SELECT * FROM users WHERE email > ?"
params = (25,)

with ExecuteQuery(query, params) as result:
    for row in result:
        print(row)