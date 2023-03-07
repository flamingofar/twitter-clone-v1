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
	e.target.style.height = "auto";
	e.target.style.height = e.target.scrollHeight + "px";
	setProgress(e);
};
const closeOnBackdrop = (e) => {
	e.stopPropagation();
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
// ------------------------------- TWEET MODAL
const tweet = async () => {
	const frm = event.target;
	const conn = await fetch("/tweet", {
		method: "POST",
		body: new FormData(frm),
	});
	const data = await conn.json();
	const epoch = Math.floor(Date.now() / 1000);

	const message = frm.querySelector("textarea[name='message']").value;
	const image = "";
	document.querySelector("[data-tweets]").insertAdjacentHTML(
		"afterbegin",
		`
		<div data-tweet data-tweet-id="${tweet["tweet_id"]}">
		<div class="flex gap-4 p-4 border-t col-span-full border-neutral-800">
			<div class="flex flex-col items-end w-1/12 gap-3 pt-1">
				<svg viewBox="0 0 24 24" aria-hidden="true" class="w-5 h-5 [&>g]:fill-neutral-800">
					<g>
						<path
							d="M12 1.75c-5.11 0-9.25 4.14-9.25 9.25 0 4.77 3.61 8.7 8.25 9.2v2.96l1.15-.17c1.88-.29 4.11-1.56 5.87-3.5 1.79-1.96 3.17-4.69 3.23-7.97.09-5.54-4.14-9.77-9.25-9.77zM13 14H9v-2h4v2zm2-4H9V8h6v2z"
						></path>
					</g>
				</svg>
				<div class="overflow-hidden rounded-full">

					<img class="w-full shrink-0" src="images/default_profile.png" alt="" />

				</div>
			</div>
			<div class="w-full">
				<span class="flex items-center gap-1"
					><span class="text-base font-bold"
						>Malte Skjoldager</span
					>
					<svg
						class="text-sky-400"
						xmlns="http://www.w3.org/2000/svg"
						width="20"
						height="20"
						fill="currentColor"
						viewBox="0 0 16 16"
					>
						<path
							d="M10.067.87a2.89 2.89 0 0 0-4.134 0l-.622.638-.89-.011a2.89 2.89 0 0 0-2.924 2.924l.01.89-.636.622a2.89 2.89 0 0 0 0 4.134l.637.622-.011.89a2.89 2.89 0 0 0 2.924 2.924l.89-.01.622.636a2.89 2.89 0 0 0 4.134 0l.622-.637.89.011a2.89 2.89 0 0 0 2.924-2.924l-.01-.89.636-.622a2.89 2.89 0 0 0 0-4.134l-.637-.622.011-.89a2.89 2.89 0 0 0-2.924-2.924l-.89.01-.622-.636zm.287 5.984l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708.708z"
						/>
					</svg>
					<span class="text-base text-gray-600"
						><strong>@</strong>"user_username" &#x2022;
						<span data-tweet-created-at> ${epoch}</span></span
					>
					<a href="#" data-close class="ml-auto group">
						<i class="text-gray-500 fa-solid fa-xmark group-hover:text-sky-400"></i>
					</a>
				</span>
				<p class="text-lg break-all">${message}</p>
				${image ? `<img class="w-full pt-2" src="./images/${image}" alt="" />` : ""}

				<div class="flex gap-14 py-4 [&>span]:cursor-pointer text-gray-500 text-sm">
					<span class="flex items-center gap-3 transition duration-500 ease-linear group">
						<i
							class="fa-regular fa-comment relative scale-x-[-1] after:absolute after:w-7 after:h-7 after:content-[''] after:-translate-x-1/2 after:-translate-y-1/2 after:top-1/2 after:left-1/2 after:rounded-full transition duration-500 after:transition after:duration-500 group-hover:after:bg-sky-400/20 group-hover:text-sky-500 group-hover:after:text-sky-500"
						></i>
						<span class="transition duration-500 ease-linear group-hover:text-sky-500"
							>0</span
						>
					</span>
					<span class="flex items-center gap-3 transition duration-500 ease-linear group">
						<i
							class="fa-solid fa-retweet relative scale-x-[-1] after:absolute after:w-7 after:h-7 after:content-[''] after:-translate-x-1/2 after:-translate-y-1/2 after:top-1/2 after:left-1/2 after:rounded-full transition duration-500 after:transition after:duration-500 group-hover:after:bg-green-400/20 group-hover:text-green-500 group-hover:after:text-green-500"
						></i>
						<span class="transition duration-500 ease-linear group-hover:text-green-500"
							>0</span
						>
					</span>
					<span class="flex items-center gap-3 transition duration-500 ease-linear group">
						<i
							class="fa-regular fa-heart relative scale-x-[-1] after:absolute after:w-7 after:h-7 after:content-[''] after:-translate-x-1/2 after:-translate-y-1/2 after:top-1/2 after:left-1/2 after:rounded-full transition duration-500 after:transition after:duration-500 group-hover:after:bg-red-400/20 group-hover:text-red-500 group-hover:after:text-red-500"
						></i>
						<span class="transition duration-500 ease-linear group-hover:text-red-500"
							>0</span
						>
					</span>
					<span class="flex items-center gap-3 transition duration-500 ease-linear group">
						<i
							class="fa-solid fa-chart-simple relative scale-x-[-1] after:absolute after:w-7 after:h-7 after:content-[''] after:-translate-x-1/2 after:-translate-y-1/2 after:top-1/2 after:left-1/2 after:rounded-full transition duration-500 after:transition after:duration-500 group-hover:after:bg-sky-400/20 group-hover:text-sky-500 group-hover:after:text-sky-500"
						></i>
						<span class="transition duration-500 ease-linear group-hover:text-sky-500"
							>0</span
						>
					</span>
					<span class="flex items-center gap-3 transition duration-500 ease-linear group">
						<i
							class="fa-solid fa-arrow-up-from-bracket relative scale-x-[-1] after:absolute after:w-7 after:h-7 after:content-[''] after:-translate-x-1/2 after:-translate-y-1/2 after:top-1/2 after:left-1/2 after:rounded-full transition duration-500 after:transition after:duration-500 group-hover:after:bg-sky-400/20 group-hover:text-sky-500 group-hover:after:text-sky-500"
						></i>
					</span>
				</div>
			</div>
		</div>
		<div class="flex gap-3 px-3 py-3 hover:bg-zinc-900">
			<div class="w-1/12 px-4"></div>
			<a href="#" class="w-full text-base text-sky-400">Show this thread</a>
		</div>
	</div>
	`
	);
	console.log(data);
};

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

if (totalTweets) totalTweets.textContent = abbrNum(totalTweets.textContent, 1);
if (totalFollowers) totalFollowers.textContent = abbrNum(totalFollowers.textContent, 2);
if (totalFollowing) totalFollowing.textContent = abbrNum(totalFollowing.textContent, 1);
