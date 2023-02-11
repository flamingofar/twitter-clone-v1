from bottle import response, post
import sqlite3

@post("/api-update-user")
def _():
    try:
        # Connect to database
        db = sqlite3.connect("twitter.db")
        id = "383d5060-f8cc-4fcd-aae2-ba917c42a4ed"

        # Set User
        db.execute("UPDATE users SET name = ? WHERE id = ? ", ("Ulla", id))
        db.commit()


        return {"success":"the user was updated"}

    except Exception as ex:
        response.status = 400
        payload = {
            "error": str(ex)
        }
        return payload
    finally:
        if "db" in locals(): db.close()
        print("############### UPDATE USER ###############")