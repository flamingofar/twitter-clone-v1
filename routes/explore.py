from bottle import get, template

@get("/explore")
def _():
    return template("explore")