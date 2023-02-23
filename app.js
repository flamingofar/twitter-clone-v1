//! TWEET ENOCH DATE CONVERTER
const convertEnoch = (createdAt, type) => {
	let month = [
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"Juli",
		"August",
		"September",
		"October",
		"November",
		"December",
	];
	let createdAtNr = +createdAt.innerText;
	console.log(createdAtNr);
	date = new Date(0);
	date.setUTCSeconds(createdAtNr);

	if (type == "tweet") return `${month[date.getUTCMonth()].substring(0, 3)} ${date.getUTCDate()}`;
	if (type == "joined") return `${month[date.getUTCMonth()]} ${date.getUTCFullYear()}`;
};
const tweets = [...document.querySelectorAll("[data-tweet]")];
const joined = document.querySelector("[data-joined]");

if (joined) joined.innerText = convertEnoch(joined, "joined");
tweets.forEach((tweet) => {
	let createdAt = tweet.querySelector("[data-tweet-created-at]");
	createdAt.innerText = convertEnoch(createdAt, "tweet");
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

//* FORMAT FOLLOWERS FOLLOWING TWEETS NUMBERS

const abbrNum = (number, decPlaces) => {
	// 2 decimal places => 100, 3 => 1000, etc
	number = Number(number);
	decPlaces = Math.pow(10, decPlaces);
	console.log(number);
	if (number < 10000) return number.toLocaleString();

	// Enumerate number abbreviations
	let abbrev = ["K", "M", "B", "T"];

	// Go through the array backwards, so we do the largest first
	for (let i = abbrev.length - 1; i >= 0; i--) {
		// Convert array index to "1000", "1000000", etc
		let size = Math.pow(10, (i + 1) * 3);

		// If the number is bigger or equal do the abbreviation
		if (size <= number) {
			// Here, we multiply by decPlaces, round, and then divide by decPlaces.
			// This gives us nice rounding to a particular decimal place.
			number = Math.round((number * decPlaces) / size) / decPlaces;

			// Handle special case where we round up to the next abbreviation
			if (number == 1000 && i < abbrev.length - 1) {
				number = 1;
				i++;
			}

			// Add the letter for the abbreviation
			number += abbrev[i];

			// We are done... stop
			break;
		}
	}

	return number;
};

const totalTweets = document.querySelector("[data-total-tweets]");
const totalFollowers = document.querySelector("[data-total-followers]");
const totalFollowing = document.querySelector("[data-total-following]");

totalTweets.textContent = abbrNum(totalTweets.textContent, 1);
totalFollowers.textContent = abbrNum(totalFollowers.textContent, 2);
totalFollowing.textContent = abbrNum(totalFollowing.textContent, 1);
