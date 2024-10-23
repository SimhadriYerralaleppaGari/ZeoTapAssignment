# src/database.py
import sqlite3

def connect_db():
    # Connect to SQLite (or any other database)
    conn = sqlite3.connect('rules.db')
    return conn

def create_table():
    # Create a table to store rules
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_text TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_rule(rule):
    # Insert a rule into the table
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Rules (rule_text) VALUES (?)', (rule,))
    conn.commit()
    conn.close()
