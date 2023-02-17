from bottle import get, template
import sqlite3
import os
import g


data = {"tweets": [
		{
			"verified": 1,
			"image_name": "1.jpg",
			"fullname": "Malte Skjoldager",
			"username": "flamingofar",
			"tweet": "The team at @Shopify recently launched an all-new marketing site, built with Tailwind CSS 😍 We just added it to our showcase to highlight some of our favorite details:",
			"tweet_image": "2.jpg",
			"total_messages": "1.2k",
			"total_retweets": "5k",
			"total_likes": "99",
			"total_graph": "45k"
		},
		{
			"verified": 0,
			"image_name": "tailwind.jpg",
			"fullname": "Santiago Donoso",
			"username": "seniordonoso",
			"tweet": "The 2023 webdev team is top notch",
			"total_messages": "1.2k",
			"total_retweets": "5k",
			"total_likes": "99",
			"total_graph": "45k"
		},
		{
			"verified": 0,
			"image_name": "codepen.jpg",
			"fullname": "Codepen",
			"username": "codepen",
			"tweet": "Checkout the new pens frem the amzing developers!",
			"total_messages": "2k",
			"total_retweets": "50k",
			"total_likes": "1.3k",
			"total_graph": "45k"
		}
	],
	"trends": [
		{
			"title": "One",
			"total_hash": 1
		},
		{
			"title": "two",
			"total_hash": 2
		},
		{
			"title": "three",
			"total_hash": 3
		},
		{
			"title": "four",
			"total_hash": 4
		}
	],
	"who_to_follow": [
		{
			"profile_image": "1.jpg",
			"full_name": "Elon Musk",
			"twitter_tag": "elonmusk"
		},
		{
			"profile_image": "codepen.jpg",
			"full_name": "Codepen",
			"twitter_tag": "codepen"
		},
		{
			"profile_image": "tailwind.jpg",
			"full_name": "TailwindCSS",
			"twitter_tag": "tailwindcss"
		}
	]
}


############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################



@get("/<username>")
def _(username):

    try:
      db = sqlite3.connect(os.getcwd()+"/twitter.db")
      db.row_factory = dict_factory
      user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE", (username,)).fetchall()[0]
      # Get the user's ID
      user_id = user["id"]
      print("#"*30)
      print(f"user id: {user}")

      # With that id, look up the repectives tweets
      tweets = db.execute("SELECT * FROM tweets JOIN users ON users.id = tweets.user_fk WHERE tweets.user_fk = ?",(user_id,)).fetchall()

      # The simple way of doing it
      # tweets = db.execute("SELECT * FROM tweets WHERE user_fk = ?", (user_id,)).fetchall()

      print("#"*60, f"\nTWEETS: {tweets}\n","#"*60)
      print(tweets)
      # Pass the tweets to the view. Template it

      # print(user)

      return template('profile', user = user, tweets=tweets, title="Twitter", name="Malte Skjoldager", trends=data["trends"], who_to_follow=data["who_to_follow"])
    except Exception as ex:
      return ex
    finally:
       if("db" in locals()): db.close()






# @get("/profile")
# def _():
#     return template('profile', title="Twitter", name="Malte Skjoldager", tweets=data["tweets"], trends=data["trends"], who_to_follow=data["who_to_follow"])