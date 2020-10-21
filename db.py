import sys
import psycopg2
from config import Config


class DB:
    def __init__(self):
        self.config = Config().as_dict()
        self.conn = self.connect()

    def connect(self):
        conn = None
        try:
            conn = psycopg2.connect(**self.config)
            print("Database connection established")
            return conn
        except psycopg2.DatabaseError as err:
            print(err)

    def disconnect(self):
        try:
            self.conn.close()
            print("Database connection closed")
        except psycopg2.DatabaseError as err:
            print(err)
            sys.exit(1)

    def get_all_feeds(self):
        try:
            cur = self.conn.cursor()
            sql_string = "SELECT * FROM feed;"
            cur.execute(sql_string)
            res = cur.fetchall()
            return res
        except psycopg2.DatabaseError as err:
            print("SELECT ERROR")
        finally:
            cur.close()

    def add_new_feed(self, name, link):
        try:
            cur = self.conn.cursor()
            sql_string = f"INSERT INTO feed (name, link) VALUES ('{name}', '{link}');"
            cur.execute(sql_string)
            return True
        except psycopg2.DatabaseError as err:
            print("INSERT ERROR", err)
        finally:
            cur.close()
