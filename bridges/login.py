from bottle import  post, response, get
import g


@post("/login")
def _():
    user ={
        "user_name": "elonmusk",
        "user_firstname": "Malte",
        "user_lastname": "Skjoldager",
    }
    response.set_cookie("user", user, secret=g.AUTH_SECRET, httponly=True)
    # Redirection
    # status code
    response.status = 302
    # the redirected page
    response.set_header("Location", "/")


    return "This is the bridge for login"

@get("/logout")
def _():
    response.delete_cookie("user", secret=g.AUTH_SECRET)
    response.status = 302
    response.set_header("Location", "/")
    return