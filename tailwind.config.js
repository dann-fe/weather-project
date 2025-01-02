/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
      colors: {
        'search-bar-color': 'rgb(165, 165, 165)',
        'primary': 'rgb(21, 59, 26)',
      },

      fontFamily: {
        LexendDeca: ['Lexend Deca'],
      },

      backgroundImage: {
        'search-icon': "url('/static/media/searchicon.svg')"
      },

      boxShadow: {
        'search-bar': '4px 3px 10.4px 3px rgba(0, 0, 0, 0.25)',
        'okres-card': '3px 4px 4.1px 2px rgba(0,0,0,0.5)',
      }
    }

  },
  plugins: [],
}

