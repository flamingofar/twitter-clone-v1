from bottle import get, template
import json
import sqlite3
import os
import g

with open('tweets.json') as tweets_json:
  data = json.load(tweets_json)

############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################



@get("/<username>")
def _(username):

    try:
      db = sqlite3.connect("/home/malteskjoldager/twitter-clone-v1")
      db.row_factory = dict_factory
      user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE", (username,)).fetchall()[0]
      # Get the user's ID
      user_id = user["id"]
      print("#"*30)
      print(f"user id: {user_id}")

      # With that id, look up the repectives tweets
      tweets = db.execute("SELECT * FROM tweets JOIN users ON users.id = tweets.user_fk WHERE tweets.user_fk = ?",(user_id,)).fetchall()

      # The simple way of doing it
      # tweets = db.execute("SELECT * FROM tweets WHERE user_fk = ?", (user_id,)).fetchall()

      print("#"*60, f"\nTWEETS: {tweets}\n","#"*60)
      print(tweets)
      # Pass the tweets to the view. Template it

      # print(user)

      return template('profile', user = user, tweets=tweets, title="Twitter", name="Malte Skjoldager", trends=data["trends"], who_to_follow=data["who_to_follow"])
    except Exception as ex:
      print(ex)
      return ex
    finally:
       if("db" in locals()): db.close()






# @get("/profile")
# def _():
#     return template('profile', title="Twitter", name="Malte Skjoldager", tweets=data["tweets"], trends=data["trends"], who_to_follow=data["who_to_follow"])