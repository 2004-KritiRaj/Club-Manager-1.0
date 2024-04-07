
// var preloader = document.querySelector('.loading');
// preloader.style.display = 'flex'; // Display the preloader

// setTimeout(function() {
//   preloader.style.display = 'none'; // Hide the preloader
// }, 5000); //5sec preloader time


var preloader = document.querySelector('.loading');
var body = document.querySelector('body');

preloader.style.display = 'flex'; // Display the preloader
body.classList.add('loading'); // Add the loading class to body to prevent scrolling

setTimeout(function() {
  preloader.style.display = 'none'; // Hide the preloader
  body.classList.remove('loading'); // Remove the loading class to enable scrolling
}, 5000); //5sec preloader time
