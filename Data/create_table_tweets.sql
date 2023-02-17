DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
    tweet_id              TEXT,
    tweet_user_fk         TEXT,
    tweet_created_at      TEXT,
    tweet_updated_at      TEXT,
    tweet_message         TEXT,
    tweet_image           TEXT,
    tweet_total_likes     TEXT,
    tweet_total_retweets  TEXT,
    tweet_total_views     TEXT,
    tweet_total_replies   TEXT,
    PRIMARY KEY(tweet_id)
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
INSERT INTO tweets VALUES(
    "939880c22d0d40ebb6475dbf657e8274",
    "cd6a5c5aee914a1abd14d880deff31e3",
    "1676644044",
    "",
    "This is a tweet from Malte",
    "",
    "0",
    "0",
    "0",
    "0"
    );