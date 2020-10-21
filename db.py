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

    def execute(self, sql_string):
        if sql_string is None:
            print("No argument supplied")
            return
        try:
            cur = self.conn.cursor()
            cur.execute(sql_string)
            res = cur.fetchone()
            return res
        except psycopg2.DatabaseError as err:
            print("Error")
        finally:
            cur.close()
