#!/usr/bin/env python3
"""
This module is used to seed the database with some initial data.
"""
from mysql.connector import connect
import uuid
import csv


def connect_db():
    """
    Connect to the database and return a connection object.
    """
    try:
        return connect(host="localhost", user="dinamow", password="password")
    except Exception as e:
        print(f"Error: '{e}'")


def create_database(connection):
    """
    Create a new database.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except Exception as e:
        print(f"Error: '{e}'")


def connect_to_prodev():
    """
    Connect to the database and return a connection object.
    """
    try:
        return connect(
            host="localhost", user="dinamow", password="password", database="ALX_prodev"
        )
    except Exception as e:
        print(f"Error: '{e}'")


def create_table(connection):
    """
    Create a new table.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user_data (
                    id VARCHAR(100) PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    age DECIMAL(3) NOT NULL
                )
            """
            )
    except Exception as e:
        print(f"Error: '{e}'")


def __read_csv(file_path):
    """
    Read a CSV file and yield each row.
    """
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row


def insert_data(connection, data):
    """
    Insert data into the table.
    """
    try:
        with connection.cursor() as cursor:
            for row in __read_csv(data):
                cursor.execute(
                    "INSERT INTO user_data (id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (str(uuid.uuid4()), row["name"], row["email"], row["age"]),
                )
            connection.commit()
    except Exception as e:
        print(f"Error: '{e}'")
