import sqlite3

class DataConn:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        """
        :return: open the database connection
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: closes the connection
        """
        self.conn.close()
        if exc_val:
            raise

if __name__ == '__main__':
    db = 'db.sqlite3'
    with DataConn(db) as conn:
        cursor = conn.cursor()