/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./node_modules/primereact/**/*.{js,ts,jsx,tsx}", "./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      backgroundColor: {
        'primary': "{{cookiecutter.bg_primary}}",
      },
      borderColor: {
        'primary-lighter': "{{cookiecutter.border_primary_lighter}}",
      },
    },
  },
  plugins: [],
};
