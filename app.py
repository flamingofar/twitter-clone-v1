from bottle import get, post, run, template, static_file, response, request
import json
import sqlite3
import uuid


############################## GET ASSETS
import assets.load_css
import assets.load_images

############################## Routes
import routes.about
import routes.contact
import routes.explore
import routes.index
import routes.profile
import routes.login
import routes.signup
import routes.error
############################## API's
# Usually API's do not return HTML. But most likely JSON
# Rule 1 - To test the API you use a HTTP client

############################## API
import api.create_user
import api.update_user
import api.delete_user
import api.get_all


############################## Server
run(host='127.0.0.1', port=3000, reloader=True, debug=True, server="paste")