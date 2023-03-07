from bottle import post, response
import sqlite3
import uuid

@post("/api-set-user")
def _():
    try:
        # Connect to database
        db = sqlite3.connect("twitter.db")
        id = str(uuid.uuid4().hex)

        # Set User
        db.execute("INSERT INTO users VALUES (?,?,?)",(id,"Magnus","Nielsen"))
        db.commit()

        print("heeeeeej")
        return {"success":"the user was created"}

    except Exception as ex:
        response.status = 400
        payload = {
            "error": str(ex)
        }
        return payload
    finally:
        if "db" in locals(): db.close()
        print("############### CREATE USER ###############")