--! Users
DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_id          TEXT,
    user_firstname   TEXT,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;

INSERT INTO users VALUES("1","A");
INSERT INTO users VALUES("2","B");

SELECT * FROM users;

--! Products
DROP TABLE IF EXISTS products;
CREATE TABLE products(
    product_id          TEXT,
    product_name        TEXT,
    product_price       TEXT,
    PRIMARY KEY(product_id)
) WITHOUT ROWID;

INSERT INTO products VALUES("1","Product A", "10");
INSERT INTO products VALUES("2","Product B", "20");

--! Orders
DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
    order_id          TEXT,
    order_user_fk     TEXT,
    order_product_fk  TEXT,
    PRIMARY KEY(order_id)
) WITHOUT ROWID;

INSERT INTO orders VALUES("1","1", "1");
INSERT INTO orders VALUES("2","1", "2");
INSERT INTO orders VALUES("3","2", "1");

--! Join users, products and orders
SELECT * FROM users
JOIN orders
JOIN products
ON user_id = order_user_fk
AND product_id = order_product_fk;

--! Average price of products
SELECT AVG(product_price) FROM products;
--! Get product containing "uct"
SELECT * FROM products WHERE product_name LIKE "%uct%";
--! Get the sum of product prices
SELECT SUM(product_price) FROM products;

SELECT * FROM users
JOIN orders
JOIN products
ON user_id = order_user_fk
AND product_id = order_product_fk
AND product_price < "15";

-- Trigger function automatically does something based on insert, update or delete. Can happen before or after.

DROP TABLE IF EXISTS customers;
CREATE TABLE customers(
    customer_id             TEXT,
    customer_firstname      TEXT,
    customer_total_tweets   TEXT,
    PRIMARY KEY(customer_id)
) WITHOUT ROWID;

INSERT INTO customers VALUES("1","A",0);


DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
    tweet_id             TEXT,
    tweet_message        TEXT,
    tweet_customer_fk    TEXT,
    PRIMARY KEY(tweet_id)
) WITHOUT ROWID;

--! TRIGGER total tweet increment based on new tweet inserted
DROP TRIGGER IF EXISTS increment_total_tweets;
CREATE TRIGGER increment_total_tweets AFTER INSERT ON tweets
BEGIN
    UPDATE customers
    SET customer_total_tweets = customer_total_tweets + 1
    WHERE customer_id = NEW.tweet_customer_fk;
END;

--! Inserting a new tweet
INSERT INTO tweets VALUES ("6", "Hi", "1");
SELECT * FROM tweets;
SELECT * FROM customers;