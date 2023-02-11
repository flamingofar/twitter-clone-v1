from bottle import post, response
import sqlite3

@post("/api-delete-user")
def _():
    try:
        # Connect to database
        db = sqlite3.connect("twitter.db")
        id = "7e449edc-bc58-4f2b-b8f3-bc5548fb550a"

        # Set User
        db.execute("DELETE FROM users WHERE id = ?", (id,))
        db.commit()


        return {"success":"the user was deleted"}

    except Exception as ex:
        response.status = 400
        payload = {
            "error": str(ex)
        }
        return payload
    finally:
        if "db" in locals(): db.close()
        print("############### DELETE USER ###############")