/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{js,jsx,ts,tsx,vue}', './index.html'],
  theme: {
    extend: {
      primary : '#243c5a', 
      secondary : {
        100: '#243c5a',
      }
    },
  },
  plugins: [],
}

