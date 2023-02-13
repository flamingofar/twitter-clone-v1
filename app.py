
from bottle import get, post, run, template, static_file, response, request, default_app
import git
import os
import g

#*############################# CONNECTS GITHUB AND PYTHONANYWHERE
@post('/13e4520155514c39be45e5d5cdac559c')
def git_update():
  repo = git.Repo('./twitter-clone-v1')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return

#*############################# GET ASSETS
import assets.load_css
import assets.load_images

#*############################# Routes
import routes.about
import routes.contact
import routes.explore
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
    g.DB_PATH=os.getcwd() + "twitter-clone-v1/twitter.db"
    application = default_app()
# Except will run on local
except Exception as ex:
    print("Running on localhost")
    run(host='127.0.0.1', port=3000, reloader=True, debug=True)