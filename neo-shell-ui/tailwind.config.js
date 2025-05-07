/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Fira Code"', "monospace"],
      },
      colors: {
        "terminal-black": "#0d0d0d",
        "terminal-green": "#33ff33",
      },
    },
  },
  plugins: [],
};
