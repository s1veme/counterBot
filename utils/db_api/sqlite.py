import sqlite3


class Database:

    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """CREATE TABLE IF NOT EXISTS users(
            id integer PRIMARY KEY AUTOINCREMENT,
            id_user text UNIQUE NOT NULL,
            username text NOT NULL,
            score integer DEFAULT 0
        )"""

        self.execute(sql, commit=True)

    def add_score_user(self, id_user, username):
        sql = """
            INSERT INTO users(id_user, username) VALUES(?, ?)
                ON CONFLICT(id_user) DO UPDATE SET score=score + 1;
        """

        self.execute(sql, parameters=(id_user, username), commit=True)

    def take_score_user(self, id_user, username):
        sql = """
            INSERT INTO users(id_user) VALUES(?, ?)
                ON CONFLICT(id_user) DO UPDATE SET score=score - 1;
        """

        self.execute(sql, parameters=(id_user, username), commit=True)

    def get_score_user(self, id_user):
        sql = """
            SELECT username, score FROM users WHERE id_user=?
        """

        return self.execute(sql, parameters=(id_user,), fetchall=True)

    def get_score_all_user(self):
        sql = """
            SELECT username, score FROM users WHERE score != 0;
        """

        return self.execute(sql, fetchall=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
