-- ! TWEETS

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
INSERT INTO tweets VALUES(
    "939880c22d0d40ebb6475dbf657e8272",
    "cd6a5c5aee914a1abd14d880deff31e3",
    "1676644044",
    "",
    "This is a tweet from Malte",
    "a0e208f43471439b855ea8ce873122aa.jpg",
    "0",
    "0",
    "0",
    "0"
    );

CREATE INDEX idx_tweets_tweet_image
ON tweets (tweet_image);


-- ! USERS
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_id                     TEXT NOT NULL UNIQUE,
    user_username               TEXT NOT NULL UNIQUE,
    user_first_name             TEXT NOT NULL ,
    user_last_name              TEXT DEFAULT "",
    user_phone_number           TEXT DEFAULT "",
    user_email                  TEXT DEFAULT "",
    user_description            TEXT,
    user_total_followers        TEXT DEFAULT 0,
    user_total_following        TEXT DEFAULT 0,
    user_total_likes            TEXT DEFAULT 0,
    user_total_tweets           TEXT DEFAULT 0,
    user_avatar                 TEXT UNIQUE,
    user_cover_image            TEXT ,
    user_created_at             TEXT NOT NULL,
    PRIMARY KEY (user_id)
) WITHOUT ROWID;


INSERT INTO users VALUES("a0e208f43471439b855ea8ce873122aa", "elonmusk", "Elon", "Musk","1", "elon@musk.com", "Bacon ipsum dolor amet filet mignon alcatra meatloaf jowl beef pastrami, turducken cow sirloin shankle spare ribs short loin beef ribs salami porchetta.", "128900000", "177","", "22700", "a0e208f43471439b855ea8ce873122aa.jpg","71ffdbb6c7a74a61b8a33ed25a6f1e58.jpeg","1676890161");

INSERT INTO users VALUES("9c5917f9220d405ba4e8f99dfced61b8", "MichelleObama", "Michelle", "Obama","2", "michelle@obama.com","Bacon ipsum dolor amet filet mignon alcatra meatloaf jowl beef pastrami, turducken cow sirloin shankle spare ribs short loin beef ribs salami porchetta.", "22200000", "17", "", "2182", "9c5917f9220d405ba4e8f99dfced61b8.jpg","","1677149378");

INSERT INTO users VALUES("04afc24ada134e1a8e928134a9926fe5", "shakira", "Shakira", "","3", "shakira@shakira.com","Bacon ipsum dolor amet filet mignon alcatra meatloaf jowl beef pastrami, turducken cow sirloin shankle spare ribs short loin beef ribs salami porchetta.", "57700000", "17", "", "7999", "04afc24ada134e1a8e928134a9926fe5.jpg","","1675594161");

INSERT INTO users VALUES("cd6a5c5aee914a1abd14d880deff31e3", "malte", "Malte", "Skjoldager","4", "malte@skjoldager.com","Bacon ipsum dolor amet filet mignon alcatra meatloaf jowl beef pastrami, turducken cow sirloin shankle spare ribs short loin beef ribs salami porchetta.", "666000", "123","", "1000","","","1672570161");

CREATE INDEX idx_users_user_first_name
ON users (user_first_name);

CREATE INDEX idx_users_user_last_name
ON users (user_last_name);

CREATE INDEX idx_users_user_avatar
ON users (user_avatar);

-- ! TRIGGER FOR INCREMENTING TOTAL TWEETS
DROP TRIGGER IF EXISTS increment_users_user_total_tweets;

CREATE TRIGGER increment_users_user_total_tweets AFTER INSERT
ON tweets
BEGIN
    UPDATE users
    SET user_total_tweets = user_total_tweets + 1
    WHERE user_id = NEW.tweet_user_fk;
END;

-- ! TRIGGER FOR DECREMENTING TOTAL TWEETS
DROP TRIGGER IF EXISTS decrement_users_user_total_tweets;

CREATE TRIGGER decrement_users_user_total_tweets AFTER DELETE
ON tweets
BEGIN
    UPDATE users
    SET user_total_tweets = user_total_tweets - 1
    WHERE user_id = OLD.tweet_user_fk;
END;

SELECT user_username, user_total_tweets FROM users;
-- Elon Musk Tweets
INSERT INTO tweets VALUES(
    "4686174f096a477aabee9046ee035854",
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

DELETE FROM tweets WHERE tweet_id = "4686174f096a477aabee9046ee035854";




-- ! TRENDS
DROP TABLE IF EXISTS trends;

CREATE TABLE trends(
    trend_id                  TEXT,
    trend_trendname           TEXT NOT NULL,
    trend_tweets_amount       TEXT DEFAULT 0,
    PRIMARY KEY (trend_id)
) WITHOUT ROWID;

INSERT INTO trends VALUES("da4e55f928fd4188a2d1913cc9070152","bikini","123");
INSERT INTO trends VALUES("da4e55f928fd4188a2d1913cc9070252","bicycle","123");
INSERT INTO trends VALUES("da4e55f928fd4188a2d1913cc9270152","bacon","123");
INSERT INTO trends VALUES("da4e55f928fd4188a2d1213cc9070152","node","123");
INSERT INTO trends VALUES("da4e55f928fd4188a2d1912cc9070152","stream_deck","123");
INSERT INTO trends VALUES("da4e55f928fd4188a221913cc9070152","sql","123");
INSERT INTO trends VALUES("da4e55f928fd418822d1913cc9070152","falling_toast","123");
INSERT INTO trends VALUES("da4e55f928fd4288a2d1913cc9070152","flamingo","123");
INSERT INTO trends VALUES("da4e55f928fd24188a2d1913cc9070152","books","123");
INSERT INTO trends VALUES("da4e55f9282fd4188a2d1913cc9070152","aqua","123");
INSERT INTO trends VALUES("da4e55f928fd4188a2d1933cc9070152","string","123");
INSERT INTO trends VALUES("da4e552928fd4188a2d1913cc9070152","bag","123");
INSERT INTO trends VALUES("da4255f928fd4188a2d1913cc9070152","looney_toons","123");


DROP VIEW IF EXISTS users_and_tweets;

CREATE VIEW users_and_tweets AS
SELECT * FROM tweets
JOIN users
ON users.user_id = tweets.tweet_user_fk;

SELECT * FROM users_and_tweets;


DROP VIEW IF EXISTS logged_in_user;

CREATE VIEW logged_in_user AS
SELECT
user_id,
user_username,
user_first_name,
user_last_name,
user_description,
user_total_followers,
user_total_following,
user_total_tweets,
user_avatar,
user_cover_image,
user_created_at
FROM users;

SELECT * FROM logged_in_user WHERE user_username = "elonmusk";


DROP VIEW IF EXISTS users_by_name_desc;
CREATE VIEW users_by_name_desc AS
    SELECT * FROM users;


SELECT * FROM users_by_name_desc ORDER BY user_first_name ASC;

SELECT name FROM sqlite_master WHERE type = 'index';
SELECT name FROM sqlite_master WHERE type = 'trigger';


SELECT * FROM users WHERE "1" COLLATE NOCASE IN (user_username, user_email, user_phone_number) ;