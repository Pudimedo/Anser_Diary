import sqlite3

def initDatabase():
    with sqlite3.connect('database/banco.db') as connection:
        with open('database/schema.sql') as schema:
            connection.executescript(schema.read()) # executescript é necessário nesse caso porque tem que criar mais de uma table no schema.sql

