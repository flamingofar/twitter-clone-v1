from bottle import get, template

@get("/contact")
def _():
    return template("contact")