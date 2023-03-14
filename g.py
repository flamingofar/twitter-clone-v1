
from bottle import request,response
import sqlite3
import pathlib
import time
import re

AUTH_SECRET = "b1f1f886-fef1-49f1-9787-0c5945dcf56fd5979325-2e99-48c4-9b82-0152e8014dbdcbfeeda8-0ff0-4fd3-8f38-8964936f45f6"



############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################

############################## GENERATE EPCOCH
epoch = str(int(time.time()))
##############################

############################## Connect to DB
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



############################## Set headers
def set_headers():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate, max-age=0")
    response.set_header("Pragma", "no-cache")
    response.set_header("Expires", "0")

############################## VALIDATE TWEET
TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 280

def validate_tweet():
    error = f"Message must be between {TWEET_MIN_LEN} and {TWEET_MAX_LEN} characters"
    if(len(request.forms.message) < TWEET_MIN_LEN):
        raise Exception(error)
    if(len(request.forms.message) > TWEET_MAX_LEN):
        raise Exception(error)
    return request.forms.get("message")

############################## DECODE URL
def decodeURL(string):
    return str(string.encode("latin-1").decode("UTF-8"))


############################## Validate username
USER_NAME_MIN = 4
USER_NAME_MAX = 15
USER_NAME_REGEX = "^[a-zA-Z0-9_]*$"
def validate_user_name():

    errorMessage = f"Username must be between {USER_NAME_MIN} and {USER_NAME_MAX} characters and can only contain letters, numbers, and underscores"
    user_name = request.forms.user_name.strip()

    # print("************",decodeURL(user_name))

    if(len(user_name) < USER_NAME_MIN):
        raise Exception(errorMessage)
    if(len(user_name) > USER_NAME_MAX):
        raise Exception(errorMessage)
    if not re.match(USER_NAME_REGEX, user_name):
        raise Exception(errorMessage)
    return