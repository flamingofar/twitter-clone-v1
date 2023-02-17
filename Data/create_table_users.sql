DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id                  TEXT NOT NULL,
    username            TEXT,
    name                TEXT NOT NULL,
    last_name           TEXT NOT NULL,
    total_followers     TEXT,
    total_following     TEXT,
    total_tweets        TEXT,
    avatar              TEXT,
    PRIMARY KEY (id)
) WITHOUT ROWID;


INSERT INTO users VALUES("a0e208f43471439b855ea8ce873122aa", "elonmusk", "Elon", "Musk", "128900000", "177", "22700", "a0e208f43471439b855ea8ce873122aa.jpg");

INSERT INTO users VALUES("9c5917f9220d405ba4e8f99dfced61b8", "MichelleObama", "Michelle", "Obama", "22200000", "17", "2182", "9c5917f9220d405ba4e8f99dfced61b8.jpg");

INSERT INTO users VALUES("04afc24ada134e1a8e928134a9926fe5", "shakira", "Shakira", "", "57700000", "17", "7999", "04afc24ada134e1a8e928134a9926fe5.jpg");

INSERT INTO users VALUES("cd6a5c5aee914a1abd14d880deff31e3", "malte", "Malte", "Skjoldager", "66600000", "123", "1000", "");