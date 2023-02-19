DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_id                  TEXT NOT NULL,
    user_username            TEXT,
    user_first_name          TEXT NOT NULL,
    user_last_name           TEXT NOT NULL,
    user_description          TEXT NOT NULL,
    user_total_followers     TEXT,
    user_total_following     TEXT,
    user_total_tweets        TEXT,
    user_avatar              TEXT,
    PRIMARY KEY (user_id)
) WITHOUT ROWID;


INSERT INTO users VALUES("a0e208f43471439b855ea8ce873122aa", "elonmusk", "Elon", "Musk", "Bacon ipsum dolor amet filet mignon alcatra meatloaf jowl beef pastrami, turducken cow sirloin shankle spare ribs short loin beef ribs salami porchetta.", "128900000", "177", "22700", "a0e208f43471439b855ea8ce873122aa.jpg");

INSERT INTO users VALUES("9c5917f9220d405ba4e8f99dfced61b8", "MichelleObama", "Michelle", "Obama","Bacon ipsum dolor amet filet mignon alcatra meatloaf jowl beef pastrami, turducken cow sirloin shankle spare ribs short loin beef ribs salami porchetta.", "22200000", "17", "2182", "9c5917f9220d405ba4e8f99dfced61b8.jpg");

INSERT INTO users VALUES("04afc24ada134e1a8e928134a9926fe5", "shakira", "Shakira", "","Bacon ipsum dolor amet filet mignon alcatra meatloaf jowl beef pastrami, turducken cow sirloin shankle spare ribs short loin beef ribs salami porchetta.", "57700000", "17", "7999", "04afc24ada134e1a8e928134a9926fe5.jpg");

INSERT INTO users(user_id, user_username, user_first_name, user_last_name, user_description, user_total_followers,user_total_following, user_total_tweets) VALUES("cd6a5c5aee914a1abd14d880deff31e3", "malte", "Malte", "Skjoldager","Bacon ipsum dolor amet filet mignon alcatra meatloaf jowl beef pastrami, turducken cow sirloin shankle spare ribs short loin beef ribs salami porchetta.", "666000", "123", "1000");