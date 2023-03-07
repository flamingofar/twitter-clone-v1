from bottle import get, template,response,request
import sqlite3
import pathlib
import g


############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################



@get("/<username>")
def _(username):
	response.set_header("Cache-Control", "no-cache, no-store, must-revalidate, max-age=0")
	response.set_header("Pragma", "no-cache")
	response.set_header("Expires", "0")

	cookie_user = request.get_cookie("user", secret=g.AUTH_SECRET)
	try:
		db = sqlite3.connect(str(pathlib.Path(__file__).parent.parent.resolve()) + "/twitter.db")
		db.row_factory = dict_factory
		user = db.execute("SELECT * FROM users WHERE user_username=? COLLATE NOCASE", (username,)).fetchall()[0]
		users = db.execute("SELECT * FROM users ORDER BY RANDOM() LIMIT 3").fetchall()
		print(users)
		# Get the user's ID
		user_id = user["user_id"]

		# With that id, look up the repectives tweets
		tweets = db.execute("SELECT * FROM tweets WHERE tweets.tweet_user_fk = ? ORDER BY tweet_created_at DESC",(user_id,)).fetchall()

		trends = db.execute("SELECT * FROM trends LIMIT 5").fetchall()

		return template('user', user = user, tweets=tweets, title="Twitter", name="Malte Skjoldager", trends=trends, who_to_follow=users, cookie_user=cookie_user)
	except Exception as ex:
		print("***************************"+str(ex))
		return ex
	finally:
		if("db" in locals()): db.close()




