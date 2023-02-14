
from bottle import post, default_app, run, static_file, get
import git
import os



#*############################# CONNECTS GITHUB AND PYTHONANYWHERE
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./twitter-clone-v1')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""

#*############################# GET ASSETS
@get(os.getcwq()+'/<filename:re:.*\.css>')
def _(filename):
    return static_file(filename, root='.')

@get('/images/<filename:re:.*\.(jpg|webp|jpeg|png)>')
def _(filename):
    return static_file(filename, root='./images')

#*############################# Routes
import routes.index
import routes.profile
import routes.login
import routes.signup
import routes.error

#*############################# API's
# Usually API's do not return HTML. But most likely JSON
# Rule 1 - To test the API you use a HTTP client
import api.create_user
import api.update_user
import api.delete_user
import api.get_all


#!################# Run on host or locally
# Try will wun in AWS
try:
    import production
    print("Running on AWS")
    application = default_app()
# Except will run on local
except Exception as ex:
    print(ex)
    print("Running on localhost")
    run(host='127.0.0.1', port=3000, reloader=True, debug=True)