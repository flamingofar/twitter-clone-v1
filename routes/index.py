from bottle import get, template
import json

with open('tweets.json') as tweets_json:
  data = json.load(tweets_json)

@get("/")
def renderIndex():
    return template('index', title="Twitter", name="Malte Skjoldager", tweets=data["tweets"], trends=data["trends"], who_to_follow=data["who_to_follow"])