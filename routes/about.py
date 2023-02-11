from bottle import get, template

@get("/about")
def _():
    return template("about")

