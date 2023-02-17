const tweets = [...document.querySelectorAll("[data-tweet]")];
let month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
tweets.forEach((tweet) => {
	let createdAt = tweet.querySelector("[data-tweet-created-at]");
	let createdAtNr = +createdAt.innerText;

	date = new Date(0);
	date.setUTCSeconds(createdAtNr);
	createdAt.innerText = `${month[date.getUTCMonth()]} ${date.getUTCDate()}`;
});
