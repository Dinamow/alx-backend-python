import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Streams user data from the ALX_prodev database in batches.

    Args:
        batch_size (int): The number of rows of user data to include in each batch.

    Yields:
        list of dict: A list of dictionaries, each representing a row of user data.
    """
    try:
        with mysql.connector.connect(
            host='localhost',
            user='dinamow',
            password='password',
            database='ALX_prodev'
        ) as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(f"SELECT * FROM user_data ORDER BY id LIMIT {batch_size};")
                while True:
                    batch = cursor.fetchone()
                    if not batch:
                        break
                    yield batch
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def batch_processing(batch_size):
    """
    Processes and prints batches of user data from the ALX_prodev database.

    Args:
        batch_size (int): The number of rows of user data to include in each batch.
    """
    for batch in stream_users_in_batches(batch_size):
        if batch['age'] > 25:
            print(batch)
    return True
