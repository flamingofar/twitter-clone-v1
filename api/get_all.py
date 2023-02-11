from bottle import get, request, response
import sqlite3
import json

@get("/api-get-all")
def _():
    try:
        payload = {
            "id":request.query.get("id"),
            "name": request.query.get("name"),
            "lastname" : request.query.get("lastname"),
        }

        if payload["id"] != "1": raise Exception("The id is wrong")
        if payload["name"] != "Malte": raise Exception("The name is wrong")
        if payload["lastname"] != "Skjoldager": raise Exception("The lastname is wrong")

        # Force exception
        # raise Exception()

        # Connect to database
        db = sqlite3.connect("twitter.db")
        cur = db.cursor()
        response.content_type = "application/json; charset=UTF-8"
        # Get User
        users = cur.execute("SELECT * FROM users LIMIT 10").fetchall()

        print(users)

        # Converting payload to a list
        # users = [dict(zip(["id", "name", "lastname"], user)) for user in users]

        # Converting list to json
        data = json.dumps(users)

        return data

    except Exception as ex:
        response.status = 400
        payload = {
            "error": str(ex)
        }
        return payload
    finally:
        if "db" in locals(): db.close()
        print("############### GET ALL ###############")