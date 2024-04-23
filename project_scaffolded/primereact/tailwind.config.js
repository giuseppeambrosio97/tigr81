/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./node_modules/primereact/**/*.{js,ts,jsx,tsx}", "./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      backgroundColor: {
        'primary': "#258900",
      },
      borderColor: {
        'primary-lighter': "rgba(0, 166, 102, 0.5)",
      },
    },
  },
  plugins: [],
};
