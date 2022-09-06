CREATE TABLE contacts (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE
)

INSERT INTO contacts (first_name, last_name, phone)
VALUES
("Andrei", "Mihalcea", "0873277327"),
("Ionut", "Mincu", "0732399421")