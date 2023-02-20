from bottle import get, template, request, redirect
import sqlite3
import os
import uuid
import time

epoch = str(int(time.time()))

############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################
@get("/tweet")
def _():
  try:
    id = str(uuid.uuid4()).replace("-","")
    test = {
      "tweet_id": id,
      "tweet_user_fk": "cd6a5c5aee914a1abd14d880deff31e3",
      "tweet_updated_at":"",
      "tweet_message":request.GET.get("message",""),
      "tweet_image":"",
      "tweet_total_likes":"0",
      "tweet_total_retweets":"0",
      "tweet_total_views":"0",
      "tweet_total_replies":"0"
    }

    db = sqlite3.connect(os.getcwd()+"/twitter.db")
    db.row_factory = dict_factory
    db.execute("""INSERT INTO tweets values(?,?,?,?,?,?,?,?,?,?)""", (
       test["tweet_id"],
       test["tweet_user_fk"],
       epoch,
       test["tweet_updated_at"],
       test["tweet_message"],
       test["tweet_image"],
       test["tweet_total_likes"],
       test["tweet_total_retweets"],
       test["tweet_total_views"],
       test["tweet_total_replies"]
       ))
    db.commit()
    print(test)
    redirect("/")
  except Exception as ex:
    print(ex)
    return ex
  finally:
    if("db" in locals()): db.close()