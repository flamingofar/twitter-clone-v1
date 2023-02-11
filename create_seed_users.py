import sqlite3
import uuid
import random
from faker import Faker

fake = Faker()
db = sqlite3.connect("twitter.db")

# Creating Table
db.executescript(
  """
  BEGIN;
  DROP TABLE IF EXISTS users;
  CREATE TABLE users(
    id        TEXT,
    name      TEXT,
    lastname  TEXT,
    email     TEXT UNIQUE,
    PRIMARY KEY(id)
  ) WITHOUT ROWID;

  COMMIT;
  """
)

# Seeding table
for x in range(100):
  id = str(uuid.uuid4())
  name = fake.first_name()
  lastname = fake.last_name()
  email = name.lower() + str(id.replace("-", "")) + fake.free_email_domain()
  db.execute("INSERT INTO users(id, name, lastname, email) VALUES(?, ?, ?, ?)",(id, name, lastname, email))
db.commit()