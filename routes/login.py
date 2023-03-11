from bottle import get, template, request

@get("/login")
def _():
    errorMessage = request.query.error
    return template('login', title="Twitter | Login", errorMessage=errorMessage)