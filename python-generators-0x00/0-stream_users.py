#!/usr/bin/env python3
import mysql.connector

def stream_users():
    """
    generator function that streams user data from the ALX_prodev database.
    """
    try:
        with mysql.connector.connect(
            host='localhost',
            user='dinamow',
            password='password',
            database='ALX_prodev'
        ) as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM user_data ORDER BY id;")
            for row in cursor:
                yield row

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")
