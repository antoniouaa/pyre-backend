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
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM feed;")
                return cur.fetchall()
        except psycopg2.DatabaseError as err:
            print("SELECT ERROR")
        finally:
            if cur:
                cur.close()

    def get_feed_by_name(self, name):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM feed WHERE name LIKE %s", (name,))
                return cur.fetchone()
        except psycopg2.DatabaseError as err:
            print("DELETE ERROR", err)
        finally:
            if cur:
                cur.close()

    def add_new_feed(self, name, link):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO feed (name, link) VALUES (%s, %s)", (name, link))
                return cur.statusmessage
        except psycopg2.DatabaseError as err:
            print("INSERT ERROR", err)
        finally:
            if cur:
                cur.close()

    def delete_feed(self, name):
        try:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM feed WHERE name=%s", (name,))
                return cur.statusmessage
        except psycopg2.DatabaseError as err:
            print("DELETE ERROR", err)
        finally:
            if cur:
                cur.close()
