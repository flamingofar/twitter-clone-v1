
from bottle import request
import sqlite3
import pathlib
import time

AUTH_SECRET = "b1f1f886-fef1-49f1-9787-0c5945dcf56fd5979325-2e99-48c4-9b82-0152e8014dbdcbfeeda8-0ff0-4fd3-8f38-8964936f45f6"

############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################

############################## GENERATE EPCOCH
epoch = str(int(time.time()))
##############################


def db():
    try:
        db=sqlite3.connect(str(pathlib.Path(__file__).parent.resolve()) + "/twitter.db")
        db.row_factory = dict_factory
        return db
    except Exception as ex:
        print(ex)
        return None
    finally:
        pass

TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 280

def validate_tweet():
    error = f"Message must be between {TWEET_MIN_LEN} and {TWEET_MAX_LEN} characters"
    if(len(request.forms.message) < TWEET_MIN_LEN):
        raise Exception(error)
    if(len(request.forms.message) > TWEET_MAX_LEN):
        raise Exception(error)
    return request.forms.get("message")