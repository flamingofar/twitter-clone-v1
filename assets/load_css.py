from bottle import get, static_file

@get('/<filename:re:.*\.css>')
def _(filename):
    return static_file(filename, root='.')