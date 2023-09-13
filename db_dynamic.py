import bcrypt
import logging
import db_utils

# Define the database path
DATABASE = "databases/dynamic.db"

# Establish a connection to the SQLite database
connection = db_utils.get_connection(DATABASE)

def initialize_database():
    """
    Initialize the database by creating necessary tables if they don't already exist.
    """
    cur = connection.cursor()

    # Check if the USERS table already exists in the database
    table_exists = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USERS'").fetchone()
    if not table_exists:
        logging.info("----- First initialization -----\n")
        _create_tables(cur)
        _create_initial_admin(cur)

    cur.close()

def _create_tables(cur):
    """
    Create the required database tables.
    """
    # List of SQL queries to create tables
    tables = [
        "CREATE TABLE USERS (username TEXT NOT NULL, passwd TEXT NOT NULL, salt TEXT NOT NULL, admin INT DEFAULT FALSE)",
        "CREATE TABLE USER_INFO (user_id INT NOT NULL, current_setting TEXT, story TEXT)",
        "CREATE TABLE CHARACTERS (user_id INT, name TEXT NOT NULL)",
        "CREATE TABLE CHARACTER_DETAILS (character_id INT NOT NULL, clan_id INT NOT NULL, background TEXT NOT NULL, physical_features TEXT NOT NULL, affinities TEXT NOT NULL)",
        "CREATE TABLE CHARACTER_STATUS (character_id INT NOT NULL, realm_id INT NOT NULL, x INT NOT NULL, y INT NOT NULL, items TEXT, skills TEXT)",
        "CREATE TABLE QUEST (quest TEXT NOT NULL)"
    ]
    # execute each table creation query
    for table_query in tables:
        cur.execute(table_query)
    logging.info(" ✓ Tables created\n")


def _create_initial_admin(cur):
    """
    Create an initial admin user with a default username and password.
    """
    username = "admin"
    password = "password"
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    # Insert the initial admin user into the USERS table
    cur.execute("INSERT INTO USERS (username, passwd, salt, admin) VALUES (?, ?, ?, ?)", (username, hashed_password, salt, True))
    logging.info(" ✓ Initial admin user created\n")

    # Commit changes to the database
    connection.commit()


# User Data
def get_user(user_id):
    return db_utils.fetch_one(connection, "SELECT username, passwd, salt FROM USERS WHERE rowid = ?;", (user_id, ))


def get_user_by_username(username):
    return db_utils.fetch_one(connection, "SELECT rowid, username, passwd, salt FROM USERS WHERE username = ?", username)


def add_user(username, password, salt):
    db_utils.execute(connection, "INSERT INTO USERS (username, passwd, salt, admin) VALUES (?, ?, ?, FALSE)", (username, password, salt))
    user_id = db_utils.fetch_one(connection, "SELECT last_insert_rowid()")[0]
    db_utils.execute(connection, "INSERT INTO USER_INFO (user_id) VALUES (?)", (user_id,))
    return user_id

def get_current_setting(user_id):
    return db_utils.fetch_one(connection, "SELECT current_setting FROM USER_INFO WHERE user_id = ?;", (user_id, ))[0]

def update_current_setting(user_id, setting):
    db_utils.execute(connection, "UPDATE USER_INFO SET current_setting = ? WHERE user_id = ?", (setting, user_id, ))


# Spell Data
def add_spell(spell):
    lines = spell.split('\n\n')
    name = lines[0].split(':')[1].strip()
    elements = lines[1].split(':')[1].strip()
    tier = lines[2].split(':')[1].strip()
    cost = int(lines[3].split(':')[1].strip())
    description = lines[4].split(':')[1].strip()

    db_utils.execute(connection, "INSERT INTO SPELLS (name, elements, tier, cost, description) VALUES (?, ?, ?, ?, ?);", name, elements, tier, cost, description)
    return db_utils.fetch_one(connection, "SELECT last_insert_rowid()")[0]

def set_mishaps(id, mishaps):
    db_utils.execute(connection, "UPDATE SPELLS SET mishaps = ? WHERE rowid = ?", (mishaps, id, ))

def get_spell(id):
    return db_utils.execute(connection, "SELECT name, elements, tier, cost, description FROM SPELLS WHERE rowid = ?", (id, ))

def get_spelllist():
    return db_utils.fetch_all(connection, "SELECT rowid, name, elements, tier, cost, description FROM SPELLS;")


# Character Data

def get_user_character(user_id, full = False):
    if full:
        sql = """SELECT c.name, cd.clan_id, cd.background, cd.physical_features, cd.affinities, cs.realm_id, cs.x, cs.y
        FROM characters c
        JOIN character_details cd
        ON c.rowid = cd.character_id
        JOIN character_status cs
        ON cd.character_id = cs.character_id
        WHERE c.user_id = ?"""
        return db_utils.fetch_one(connection, sql, (user_id,))
    else:
        return db_utils.fetch_one(connection, "SELECT user_id, name FROM CHARACTERS WHERE rowid = ?;", (user_id, ))

def get_character(character_id, full = False):
    if full:
        sql = """SELECT c.name, cd.clan_id, cd.background, cd.physical_features, cd.affinities, cs.realm_id, cs.x, cs.y
        FROM characters c
        JOIN character_details cd
        ON c.rowid = cd.character_id
        JOIN character_status cs
        ON cd.character_id = cs.character_id
        WHERE cd.character_id = ?"""
        return db_utils.fetch_one(connection, sql, (character_id,))
    else:
        return db_utils.fetch_one(connection, "SELECT user_id, name FROM CHARACTERS WHERE rowid = ?;", (character_id, ))

def get_character_id(name):
    sql = "SELECT rowid FROM CHARACTERS WHERE name = ?;"
    if db_utils.fetch_one(connection, sql, (name,)) is not None:
        return db_utils.fetch_one(connection, sql, (name,))[0]
    else:
        return None

def get_character_by_name(character_name, full = False):
    if full:
        sql = """SELECT c.name, cd.clan_id, cd.background, cd.physical_features, cd.affinities, cs.realm_id, cs.x, cs.y
        FROM characters c
        JOIN character_details cd
        ON c.rowid = cd.character_id
        JOIN character_status cs
        ON cd.character_id = cs.character_id
        WHERE c.character_name = ?"""
        db_utils.execute(connection, sql, (character_name,))

def add_character(clan_id, name, background, physical_features, affinities, realm_id, x, y, user_id):
    db_utils.execute(connection, "INSERT INTO CHARACTERS (user_id, name) VALUES (?, ?);", (user_id, name))
    character_id = db_utils.fetch_one(connection, "SELECT last_insert_rowid()")[0]
    db_utils.execute(connection, "INSERT INTO CHARACTER_DETAILS (character_id, clan_id, background, physical_features, affinities) VALUES (?, ?, ?, ?, ?)", (character_id, clan_id, background, physical_features, affinities, ))
    db_utils.execute(connection, "INSERT INTO CHARACTER_STATUS (character_id, realm_id, x, y) VALUES (?, ?, ?, ?)", (character_id, realm_id, x, y, ))
    return character_id

def set_character_location(character_id, realm_id, x, y):
    db_utils.execute(connection, "UPDATE CHARACTER_STATUS SET realm_id = ?, x = ?, y = ? WHERE character_id = ?", (realm_id, x, y, character_id, ))

def set_character_items(character_id, items):
    db_utils.execute(connection, "UPDATE CHARACTER_STATUS SET items = ? WHERE character_id = ?", (items, character_id, ))

def get_character_items(character_id):
    return db_utils.fetch_one(connection, "SELECT items FROM CHARACTER_STATUS WHERE rowid = ?;", (character_id, ))

def set_character_skills(character_id, skills):
    db_utils.execute(connection, "UPDATE CHARACTER_STATUS SET skills = ? WHERE character_id = ?", (skills, character_id, ))

def get_character_skills(character_id):
    return db_utils.fetch_one(connection, "SELECT skills FROM CHARACTER_STATUS WHERE rowid = ?;", (character_id, ))


# Quest data

def get_quest():
    if db_utils.fetch_one(connection, "SELECT quest FROM QUESTS") is None: return None
    return db_utils.fetch_one(connection, "SELECT quest FROM QUESTS")[0]

def update_quest(quest):
    db_utils.execute(connection, "UPDATE QUESTS SET quest = ?", (quest, ))

def add_quest(quest):
    db_utils.execute(connection, "INSERT INTO QUESTS (quest) VALUES (?);", (quest, ))


# Story data

def get_story(user_id):
    return db_utils.fetch_one(connection, "SELECT story FROM USER_INFO WHERE user_id = ?", (user_id, ))[0]

def update_story(user_id, story):
    db_utils.execute(connection, "UPDATE USER_INFO SET story = ? WHERE user_id = ?", (story, user_id, ))
