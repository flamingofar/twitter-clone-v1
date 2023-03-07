from bottle import post, default_app, run, static_file, get
import git

# This is a git test

#*############################# CONNECTS GITHUB AND PYTHONANYWHERE
@post('/13e4520155514c39be45e5d5cdac559c')
def git_update():
  repo = git.Repo('./twitter-clone-v1')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""

#*############################# GET ASSETS
import assets.load_js
import assets.load_css
import assets.load_images

#*############################# Routes
import routes.index
import routes.user
import routes.login
import routes.signup
import routes.error
import routes.to_follow
import routes.profile

#*############################# API's
# Usually API's do not return HTML. But most likely JSON
# Rule 1 - To test the API you use a HTTP client
import api.create_user
import api.update_user
import api.delete_user
import api.get_all
import api.create_tweet
import api.delete_tweet

#*############################# BRIDGES
import bridges.login


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
    run(host='127.0.0.1', port=4000, reloader=True, debug=True, server="paste")