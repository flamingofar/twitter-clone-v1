DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
    id              TEXT,
    user_fk         TEXT,
    created_at      TEXT,
    updated_at      TEXT,
    message         TEXT,
    image           TEXT,
    total_likes     TEXT,
    total_retweets  TEXT,
    total_views     TEXT,
    total_replies   TEXT,
    PRIMARY KEY(id)
) WITHOUT ROWID;

-- Elon Musk Tweets
INSERT INTO tweets VALUES(
    "1686174f096a477aabee9046ee035854",
    "a0e208f43471439b855ea8ce873122aa",
    "1676283236",
    "",
    "This is a tweet from Elon",
    "",
    "0",
    "0",
    "0",
    "0"
    );

INSERT INTO tweets VALUES(
    "b23c016faac04a278e27635a1a00403c",
    "a0e208f43471439b855ea8ce873122aa",
    "1676283236",
    "",
    "This is a tweet from Elon number 2",
    "",
    "0",
    "0",
    "0",
    "0"
    );
-------------------------------------------------

INSERT INTO tweets VALUES(
    "cd0d40cfb15b4d9bbd7a693803af9927",
    "04afc24ada134e1a8e928134a9926fe5",
    "1676283236",
    "",
    "This is a tweet Shakira",
    "",
    "0",
    "0",
    "0",
    "0"
    );