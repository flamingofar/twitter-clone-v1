import sqlite3
import uuid
import random
from faker import Faker

fake = Faker()
db = sqlite3.connect("company.db")

# Creating Table
db.executescript(
  """
  BEGIN;
  DROP TABLE IF EXISTS customers;
  CREATE TABLE customers(
    id                  TEXT,
    customer_firstname  TEXT,
    customer_total_tweets TEXT,
    PRIMARY KEY(id)
  ) WITHOUT ROWID;

  COMMIT;
  """
)

# Seeding table
for x in range(1000000):
  id = str(uuid.uuid4())
  customer_firstname = fake.first_name()
  customer_total_tweets = "1"
  db.execute("INSERT INTO customers(id, customer_firstname, customer_total_tweets) VALUES(?, ?, ?)",(id, customer_firstname, customer_total_tweets))
db.commit()