from bottle import get, static_file
import os

@get('/<filename:re:.*\.css>')
def _(filename):
    return static_file(filename, root=os.getcwd())