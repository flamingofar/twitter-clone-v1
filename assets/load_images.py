from bottle import get, static_file
import os

@get('/images/<filename:re:.*\.(jpg|webp|jpeg|png)>')
def _(filename):
    return static_file(filename, root=os.getcwd()+'/images')