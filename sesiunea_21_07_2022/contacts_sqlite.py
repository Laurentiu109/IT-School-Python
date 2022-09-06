from msilib.schema import Error
import pathlib
import sqlite3
import logging
import sys

ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("dev.db")

# configure logger
logging.root.setLevel(logging.DEBUG)
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s")

def create_contacts_table(connection):
    if not isinstance(connection, sqlite3.Connection):
        raise TypeError("Not a DB connection object.")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts  (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE
        )
    """)
    connection.commit()

def add_contact(first_name, last_name, phone, connection):
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO contacts (first_name, last_name, phone)
    VALUES
    ("Andrei", "Mihalcea", "0873277327")
    """)
    connection.commit()

# init db
try:
    con = sqlite3.connect(DB_FILE)

except sqlite3.Error as err:
    logging.critical(err)
    sys.exit(1)

# init schema
try:
    create_contacts_table(con)
except (sqlite3.Error, TypeError) as err:
    logging.critical(err)
else:

# DB operations
    try:
        add_contact(None, None, None, con)
    except sqlite3.Error as err:
        logging.error(err)
# close db

con.close()