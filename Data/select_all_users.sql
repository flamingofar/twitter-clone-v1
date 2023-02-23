SELECT * FROM users;

SELECT * FROM users JOIN tweets ON users.user_id = tweets.tweet_user_fk WHERE tweets.tweet_user_fk = "cd6a5c5aee914a1abd14d880deff31e3" ORDER BY tweet_created_at DESC;