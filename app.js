//! TWEET ENOCH DATE CONVERTER
const tweets = [...document.querySelectorAll("[data-tweet]")];
let month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
tweets.forEach((tweet) => {
	let createdAt = tweet.querySelector("[data-tweet-created-at]");
	let createdAtNr = +createdAt.innerText;

	date = new Date(0);
	date.setUTCSeconds(createdAtNr);
	createdAt.innerText = `${month[date.getUTCMonth()]} ${date.getUTCDate()}`;
});

//! TWEET MODAL
const tweetModalTextArea = document.querySelector("[data-tweet-modal] textarea");
const tweetModalClose = document.querySelector("[data-tweet-modal-close]");
const tweetModalContainer = document.querySelector("[data-tweet-modal-container]");
const tweetCharacterProgress = document.querySelector("[data-tweet-modal-container]");
const tweetMenuButton = document.querySelector("[data-tweet-button-menu]");

const textareaAutoGrow = (e) => {
	console.log(e.target);
	e.target.style.height = "auto";
	e.target.style.height = e.target.scrollHeight + "px";
	setProgress(e);
};
const closeOnBackdrop = (e) => {
	e.stopPropagation();
	console.log(e);
	// this.classList.add("hidden");
};

tweetModalTextArea.addEventListener("input", textareaAutoGrow);

tweetModalContainer.addEventListener("click", (e) => {
	if (e.target.classList.contains("backdrop")) {
		e.target.classList.add("hidden");
	}
});

tweetMenuButton.addEventListener("click", () => {
	tweetModalContainer.classList.remove("hidden");
});
tweetModalClose.addEventListener("click", () => {
	tweetModalContainer.classList.add("hidden");
	tweetModalTextArea.value = "";
});

const setProgress = () => {
	let textLength = tweetModalTextArea.value.length;
	let maxChar = 280;
	let charUsed = (100 * textLength) / maxChar;
	let charUsedInDeg = (100 * textLength) / maxChar;
	let charLeft = ((maxChar - textLength) / 280) * 100;

	tweetCharacterProgress.style.setProperty("--progress", charUsedInDeg + "deg");
	tweetCharacterProgress.style.setProperty("--total-characters", charLeft + "%");
	tweetCharacterProgress.style.setProperty("--used-characters", charUsed + "%");

	if (textLength >= maxChar) {
		document.querySelector(".character_progress").style.setProperty("--progress-bg", "black");
		document
			.querySelector(".character_progress")
			.setAttribute("data-char-exceed", maxChar - textLength);
	} else {
		document.querySelector(".character_progress").setAttribute("data-char-exceed", "");
		document
			.querySelector(".character_progress")
			.style.setProperty("--progress-bg", "rgb(14 165 233)");
	}
};

let form = document.querySelector("[data-tweet-modal] form");
form.addEventListener("submit", (e) => {
	e.preventDefault();
	e.target.submit();
});

//* REMOVE TWEET
tweets.forEach((tweet) => {
	tweet.querySelector("button").addEventListener("click", () => {
		const tweetID = tweet.dataset.tweetId;
		tweet.classList.add("hidden");
		console.log(tweetID);
		deleteTweetDB(tweet);
	});
});

// const deleteTweetDB = async (id) => {
// 	fetch("/delete-tweet", {
// 		method: "POST",
// 		headers: {
// 			Accept: "application/json",
// 			"Content-Type": "application/json",
// 		},
// 		body: JSON.stringify({ id: id }),
// 	});
// };
