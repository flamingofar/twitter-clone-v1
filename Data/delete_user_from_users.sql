DELETE FROM users
WHERE id = "cd6a5c5aee914a1abd14d880deff31e3";

SELECT * FROM tweets
JOIN users
ON users.user_id = tweets.tweet_user_fk
;

SELECT * FROM users ORDER BY RANDOM() LIMIT 3;