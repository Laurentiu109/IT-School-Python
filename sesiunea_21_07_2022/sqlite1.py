import pathlib
import sqlite3

ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("dev.db")

# 1. conectarea la baza de date

con = sqlite3.connect(DB_FILE)

# 2. Creare cursor

cur = con.cursor()

# 3. Compunere QUERY (interogare baze de date)

# Creare tabel
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts  (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE
)
""")

# Insert
cur.execute("""
INSERT INTO contacts (first_name, last_name, phone)
VALUES
("Andrei", "Mihalcea", "0873277327"),
("Ionut", "Mincu", "0732399421")
""")

# 4. Commit - executarea query pe baza de date
con.commit()