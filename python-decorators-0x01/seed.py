#!/usr/bin/env python3
"""
This module is used to seed the database with some initial data.
"""
import sqlite3
import uuid
import csv
from typing import Tuple

def user_data():
    """
    Returns a list of tuples representing user data.
    """
    with open('user_data.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            yield (str(uuid.uuid4()), *row)

def insert_data():
    """
    Inserts the given data into the database.
    """
    table_q = """
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age TEXT NOT NULL
    )
    """
    insert_q = """
    INSERT INTO users (id, name, email, age)
    VALUES (?, ?, ?, ?)
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(table_q)
    for data in user_data():
        cursor.execute(insert_q, data)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_data()