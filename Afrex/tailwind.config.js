/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
	  './Chat/templates/pages/*.html',
	  /* this above is the path to the directory of my template(html) files*/
  ],
  theme: {
    extend: {
      height: {
        '120': '40rem', //customizing my height value
      },
      width: {
        '120': '40rem', //customized my width value
      },
      colors: {
        'translucent-gray': 'rgba(110, 110, 110, 0.25)', //  i intend to use this for the login and signup page
        'coral-pink': '#ff7474',
      },
      fontFamily: {
        'magnolia': ['Magnolia Script', 'cursive'],
      }
    },
  },
  plugins: [],
}

