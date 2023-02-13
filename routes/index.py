from bottle import get, template

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

@get("/")
def _():
    return template('index', title="Twitter", name="Malte Skjoldager", tweets=data["tweets"], trends=data["trends"], who_to_follow=data["who_to_follow"])