import sqlite3
from flask import g

def connect_to_database():
    # Get the database connection from the context-local proxy g
    if 'db' not in g:
        g.db = sqlite3.connect('dbClubsync.db')

def get_database():
    # Get the database connection from the context-local proxy g
    if 'db' not in g:
        connect_to_database()
    return g.db

def close_connection():
    # Close the database connection if it exists in the context-local proxy g
    db = g.pop('db', None)
    if db is not None:
        db.close()

def create_table():
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clubs (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    college TEXT,
                    venue TEXT)''')
    db.commit()

def insert_data(name, college, venue):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO clubs (name, college, venue) VALUES (?, ?, ?)''', (name, college, venue))
    db.commit()

def fetch_clubs():
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM clubs''')
    rows = cursor.fetchall()
    return rows

def update_data(id, name, college, venue):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''UPDATE clubs SET name=?, college=?, venue=? WHERE id=?''', (name, college, venue, id))
    db.commit()

def delete_data(id):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''DELETE FROM clubs WHERE id=?''', (id,))
    db.commit()

def delete_table():
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''DROP TABLE IF EXISTS clubs''')
    db.commit()

def fetch_table_names():
    db = get_database()
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return tables
