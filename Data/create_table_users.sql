-- DROP table users;

CREATE TABLE users(
    id TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    PRIMARY KEY (id)
) WITHOUT ROWID