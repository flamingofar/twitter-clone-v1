from bottle import post, template, request, redirect,response
import sqlite3
import os
import uuid
import pathlib
import urllib.parse

import g



def decodeURL(string):
    return str(string.encode("latin-1").decode("UTF-8"))



@post("/tweet")
def _():
  try:
    g.validate_tweet()
    db = g.db()
    tweet_id = str(uuid.uuid4().hex)
    tweet_user_fk = "a0e208f43471439b855ea8ce873122aa"
    print(type(tweet_user_fk))
    tweet_created_at = g.epoch
    tweet_updated_at = ""
    tweet_message = decodeURL(request.forms.get("message"))
    tweet_image = ""
    tweet_total_likes = "0"
    tweet_total_retweets = "0"
    tweet_total_views = "0"
    tweet_total_replies = "0"

    db.execute("INSERT INTO tweets VALUES(?,?,?,?,?,?,?,?,?,?)",(
      tweet_id,
      tweet_user_fk,
      tweet_created_at,
      tweet_updated_at,
      tweet_message,
      tweet_image,
      tweet_total_likes,
      tweet_total_retweets,
      tweet_total_views,
      tweet_total_replies)
      )

    db.commit()
    return {"info":"Tweet created successfully",
            "tweet_id":tweet_id}
  except Exception as ex:
    print(ex)
    response.status = 400
    return {"info":str(ex)}

  finally:
    pass
