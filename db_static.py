import logging
import db_utils

# Define the database path
DATABASE = "databases/static.db"

# Establish a connection to the SQLite database
connection = db_utils.get_connection(DATABASE)

def initialize_database():
    """
    Initialize the database by creating necessary tables if they don't already exist.
    """
    cur = connection.cursor()

    # Check if the REALM table already exists in the database
    table_exists = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='REALM'").fetchone()
    if not table_exists:
        logging.info("----- Initializing static database -----\n")
        _create_tables(cur)
    else:
        logging.info("----- Static database already exists -----\n")
    cur.close()

def _create_tables(cur):
    """
    Create the required database tables using SQL scripts.
    """
    # Load SQL scripts to create tables
    with open("databases/static_scripts/REALM.sql", 'r') as realm_sql:
        cur.executescript(realm_sql.read())
    logging.info(" ✓ REALM table created\n")

    with open("databases/static_scripts/RACES.sql", 'r') as races_sql:
        cur.executescript(races_sql.read())
    logging.info(" ✓ RACES table created\n")

    # Commit changes to the database
    connection.commit()

# Realm Data
def add_realm(name, setting, history):
    db_utils.execute(connection, "INSERT INTO REALMS (name, setting, history) VALUES (?, ?, ?);", (name, setting, history, ))
    return db_utils.fetch_one(connection, "SELECT last_insert_rowid()")[0]

def get_name(realm = 1):
    return db_utils.fetch_one(connection, "SELECT name FROM REALMS WHERE rowid = ?;", (realm, ))[0]

def get_setting(realm = 1):
    return db_utils.fetch_one(connection, "SELECT setting FROM REALMS WHERE rowid = ?;", (realm, ))[0]

def get_history(realm = 1):
    return db_utils.fetch_one(connection, "SELECT history FROM REALMS WHERE rowid = ?;", (realm, ))[0]

def get_realm(realm_id = 1):
    return db_utils.fetch_one(connection, "SELECT name, setting, history FROM REALMS WHERE rowid = ?;", (realm_id, ))

# Race data
def get_race(race_id = 1):
    return db_utils.fetch_one(connection, "SELECT race")