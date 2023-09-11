import sqlite3

def get_connection(db_path: str) -> sqlite3.Connection:
    """
    Get a connection to the SQLite database at the specified path.

    Parameters:
    - db_path (str): The path to the SQLite database file.

    Returns:
    - sqlite3.Connection: A connection object to the SQLite database.
    """
    return sqlite3.connect(db_path)

def fetch_one(connection: sqlite3.Connection, query: str, *args) -> tuple:
    """
    Fetch a single result from the database using the provided query.

    Parameters:
    - connection (sqlite3.Connection): The database connection object.
    - query (str): The SQL query to execute.
    - *args (tuple): Optional values to be used in the query's placeholders.

    Returns:
    - tuple: A single record from the database or None if no record is found.
    """
    with connection as conn:
        return conn.execute(query, *args).fetchone()

def fetch_all(connection: sqlite3.Connection, query: str, *args) -> list:
    """
    Fetch all results from the database using the provided query.

    Parameters:
    - connection (sqlite3.Connection): The database connection object.
    - query (str): The SQL query to execute.
    - *args (tuple): Optional values to be used in the query's placeholders.

    Returns:
    - list of tuples: A list of records from the database.
    """
    with connection as conn:
        return conn.execute(query, *args).fetchall()

def execute(connection: sqlite3.Connection, query: str, *args) -> None:
    """
    Execute a given SQL query.

    Parameters:
    - connection (sqlite3.Connection): The database connection object.
    - query (str): The SQL query to execute.
    - *args (tuple): Optional values to be used in the query's placeholders.

    This function does not return any value.
    """
    with connection as conn:
        conn.execute(query, *args)
