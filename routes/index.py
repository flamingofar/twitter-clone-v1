from bottle import get, template,response,request
import sqlite3
import pathlib
import g
import traceback





############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################





@get("/")
def _():
	response.set_header("Cache-Control", "no-cache, no-store, must-revalidate, max-age=0")
	response.set_header("Pragma", "no-cache")
	response.set_header("Expires", "0")

	cookie_user = request.get_cookie("user", secret=g.AUTH_SECRET)
	try:

		db = sqlite3.connect(str(pathlib.Path(__file__).parent.parent.resolve()) + "/twitter.db")
		db.row_factory = dict_factory
		user = db.execute("SELECT * FROM users WHERE user_username=? COLLATE NOCASE", (cookie_user["user_name"],)).fetchall()[0] if cookie_user else None
		users = db.execute("SELECT * FROM users ORDER BY RANDOM() LIMIT 3").fetchall()
		tweets = db.execute("SELECT * FROM users_and_tweets ORDER BY tweet_created_at DESC").fetchall()
		trends = db.execute("SELECT * FROM trends LIMIT 7").fetchall()
		print(trends)

		return template('index', tweets=tweets, title="Twitter", name="Malte Skjoldager", trends=trends, who_to_follow=users, user=user, cookie_user=cookie_user)
	except Exception as ex:
		traceback.print_exc()
		print("**************** EXCEPTION! ", ex)
		return ex
	finally:
		if("db" in locals()): db.close()
