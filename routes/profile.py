from bottle import get, template, response,request
import sqlite3
import pathlib
import g


############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################



@get("/profile")
def _():
    g.set_headers()

    cookie_user = request.get_cookie("user", secret=g.AUTH_SECRET)
    try:
        db = g.db()
        user = db.execute("SELECT * FROM logged_in_user WHERE user_username = ? COLLATE NOCASE", (cookie_user["user_username"],)).fetchall()[0]
        print("*************************** USER: ",user)

        users = db.execute("SELECT * FROM users ORDER BY RANDOM() LIMIT 3").fetchall()
        # Get the user's ID
        user_id = user["user_id"]

        # With that id, look up the repectives tweets
        tweets = db.execute("SELECT * FROM tweets WHERE tweets.tweet_user_fk = ? ORDER BY tweet_created_at DESC",(user_id,)).fetchall()

        trends = db.execute("SELECT * FROM trends LIMIT 5").fetchall()

        return template('profile', user = user, tweets=tweets, title="Twitter", name="Malte Skjoldager", trends=trends, who_to_follow=users)
    except Exception as ex:
        print("***************************"+str(ex))
        return ex
    finally:
        if("db" in locals()): db.close()




