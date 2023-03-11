from bottle import  post, response, get,request
import g
import time


@post("/login")
def _():
    try:

        login_input = request.forms.get("login_input")
        if not login_input:
            raise Exception("Username not found")

        db = g.db()

        user = db.execute(" SELECT * FROM users WHERE ? COLLATE NOCASE IN (user_username, user_email, user_phone_number)", (login_input,)).fetchall()[0]
        print("THIS IS THE USER!!", user)


        response.set_cookie("user", user, secret=g.AUTH_SECRET, httponly=True, expires=(time.time() + 86400) )
        # Redirection
        # status code
        response.status = 302
        # the redirected page
        response.set_header("Location", "/")


        return "This is the bridge for login"
    except Exception as ex:
        print(str(ex))
        response.status = 302
        response.set_header("Location", "/?error=We could not find that username.")
        return
    finally:
        if("db" in locals()): db.close()




@get("/logout")
def _():
    response.delete_cookie("user", secret=g.AUTH_SECRET)
    response.status = 302
    response.set_header("Location", "/")
    return