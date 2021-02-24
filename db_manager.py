import sqlite3

_RETRY_LIMIT = 5

def _get_connection(db_path):
    exception = None
    for i in range(_RETRY_LIMIT):
        try:
            return sqlite3.connect(db_path)
        except Exception as e:
            exception = e
    print(f'Error! Could not connect to database at {db_path}. See exception:\n{exception}')
    return None

def _create_table(conn, create_table_sql):
    exception = None
    for i in range(_RETRY_LIMIT):
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
            return cursor
        except Exception as e:
            exception = e
    print('Error! Could not create database.')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(create_table_sql)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'See exception:\n{exception}')
    return None

# Create a SQLite database if it doesn't exist.
# Returns the datbase connection and cursor.
def startup_database(db_path, create_table_sql):
    conn = _get_connection(db_path)
    if conn is not None:
        cursor = _create_table(conn, create_table_sql)
        return conn, cursor
    return None, None
