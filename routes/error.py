from bottle import error, template

@error(404)
def _(error):
    return template("error")
