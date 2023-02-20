from bottle import get, response,redirect
import sqlite3

@get("/delete-tweet/<tweet_id>")
def _(tweet_id):
    try:
        # Connect to database
        db = sqlite3.connect("twitter.db")
        # id = "7e449edc-bc58-4f2b-b8f3-bc5548fb550a"

        # Delete Tweet
        db.execute("DELETE FROM tweets WHERE tweet_id = ?", (tweet_id,))
        db.commit()


        redirect("/")

    except Exception as ex:
        print(ex)
        return ex
        response.status = 400
        payload = {
            "error": str(ex)
        }
        return payload
    finally:
        # if "db" in locals(): db.close()
        print("############### DELETE USER ###############")