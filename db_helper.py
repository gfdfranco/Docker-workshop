#python3 -m pip install psycopg2
import psycopg2
import os

class DatabaseHelper:

    def __init__(self):
        self._conn = self._connectionDB()

    def _connectionDB(self):
        conn = psycopg2.connect(
            database="pruebas",
            user='postgres',
            password='postgres',
            host='192.168.100.9',
            port='5432'
        )
        return conn

    def _closeConnectionDB(self):
        self._conn.close()

    def create_users_table(self):
        sql = '''CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )'''
        cur = self._conn.cursor()
        cur.execute(sql)
        self._conn.commit()
        cur.close()


    def insert_values_users_table(self, name):
        sql = "INSERT INTO users(name) VALUES(%s)"
        cur = self._conn.cursor()
        cur.execute(sql, (name,))
        self._conn.commit()
        cur.close()
        self._closeConnectionDB()