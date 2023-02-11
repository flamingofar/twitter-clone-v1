/** @type {import('tailwindcss').Config} */
module.exports = {
	mode: "jit",
	content: ["../**/*.html"],
	theme: {
		extend: {
			fontFamily: {
				sans: ["seque", "ui-sans-serif", "system-ui"],
			},
			boxShadow: {
				chat: "0px -2px 10px 1px rgba(255,255,255,0.48)",
			},
		},
	},
	plugins: [],
};
