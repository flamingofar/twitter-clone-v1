from bottle import get, static_file

@get('/images/<filename:re:.*\.(jpg|webp|jpeg)>')
def _(filename):
    return static_file(filename, root='./images')