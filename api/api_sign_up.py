from bottle import post, request, response
import uuid
import g

#*#############################
@post('/api-sign_up')
def _():
    try:
        user_name = g.validate_user_name()
        user_id = uuid.uuid4().hex
        user = {
            "user_id": user_id,
            "user_name": user_name,

        }
        values = ""
        for key in user:
            values += f":{key},"
        values = values.rstrip(",")
        print(values)
        # db = g.db()
        # db.execute(f"INSERT INTO users VALUES({values})", user)
        return {"data":"ok"}
    except Exception as ex:
        print(ex)
        response.status = 400
        return {"info": "error", "message": str(ex)}
    finally:
        if "db" in locals():
            db.close()