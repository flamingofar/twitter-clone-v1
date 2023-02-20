from bottle import get, template
import sqlite3
import pathlib





############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################

data = {
	"trends": [
		{
			"title": "One",
			"total_hash": 1
		},
		{
			"title": "two",
			"total_hash": 2
		},
		{
			"title": "three",
			"total_hash": 3
		},
		{
			"title": "four",
			"total_hash": 4
		}
	],
	"who_to_follow": [
		{
			"profile_image": "1.jpg",
			"full_name": "Elon Musk",
			"twitter_tag": "elonmusk"
		},
		{
			"profile_image": "codepen.jpg",
			"full_name": "Codepen",
			"twitter_tag": "codepen"
		},
		{
			"profile_image": "tailwind.jpg",
			"full_name": "TailwindCSS",
			"twitter_tag": "tailwindcss"
		}
	]
}



@get("/")
def _():
	try:

		db = sqlite3.connect(str(pathlib.Path(__file__).parent.parent.resolve()) + "/twitter.db")
		db.row_factory = dict_factory
		users = db.execute("SELECT * FROM users ORDER BY RANDOM() LIMIT 3").fetchall()
		tweets = db.execute("SELECT * FROM tweets JOIN users ON users.user_id = tweets.tweet_user_fk ORDER BY tweet_created_at DESC").fetchall()

		return template('index', tweets=tweets, title="Twitter", name="Malte Skjoldager", trends=data["trends"], who_to_follow=users)
	except Exception as ex:
		print(ex)
		return ex
	finally:
		if("db" in locals()): db.close()
