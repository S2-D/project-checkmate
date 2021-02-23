//show tutorial 
if (localStorage) {
  var visits_dashboard = localStorage.getItem('visits_dashboard');
  console.log(visits_dashboard);
  if (visits_dashboard == null) {
    console.log("welcome!")
    tutorial();
    localStorage.setItem("visits_dashboard", "first_visit");
    var visits_dashboard = localStorage.getItem('visits_dashboard');
  } else {
    localStorage.setItem("visits_dashboard", "visited");
  }
}

function tutorial () {
  $(document).ready(function(){
      $(".modal").fadeIn();
      show_tutorial_slides(tutor_slideIndex);
  });
}

$(function(){ 
  $("#tutor_close_btn").click(function(){
    $(".modal").fadeOut();
  });
})

var todayContainer = document.querySelector(".today");
var d = new Date();
var weekday = new Array(7);
weekday[0] = "Sunday 🖖";
weekday[1] = "Monday 💪😀";
weekday[2] = "Tuesday 😜";
weekday[3] = "Wednesday 😌☕️";
weekday[4] = "Thursday 🤗";
weekday[5] = "Friday 🍻";
weekday[6] = "Saturday 😴";

var n = weekday[d.getDay()];

var randomWordArray = Array(
  "Oh my, it's ",
  "Whoop, it's ",
  "Happy ",
  "Seems it's ",
  "Awesome, it's ",
  "Have a nice ",
  "Happy fabulous ",
  "Enjoy your "
);
var randomWord =
  randomWordArray[Math.floor(Math.random() * randomWordArray.length)];
todayContainer.innerHTML = randomWord + n;

// prgress
const progress = document.querySelector(".progress-done");

progress.style.width = progress.getAttribute("data-done") + "%";
progress.style.opacity = 1;

// 이미지슬라이드
var slideIndex = 0; //slide index

// HTML 로드가 끝난 후 동작
window.onload = function () {
  showSlides(slideIndex);

  // Auto Move Slide
  var sec = 3000;
  setInterval(function () {
    slideIndex++;
    showSlides(slideIndex);
  }, sec);
};

// Next/previous controls
function moveSlides(n) {
  slideIndex = slideIndex + n;
  showSlides(slideIndex);
}

// Thumbnail image controls
function currentSlide(n) {
  slideIndex = n;
  showSlides(slideIndex);
}

function showSlides(n) {
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  var size = slides.length;

  if (n + 1 > size) {
    slideIndex = 0;
    n = 0;
  } else if (n < 0) {
    slideIndex = size - 1;
    n = size - 1;
  }

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  slides[n].style.display = "block";
  dots[n].className += " active";
}

// 튜토리얼 이미지슬라이드
var tutor_slideIndex = 0; //slide index

// Next/previous controls
function tutor_moveSlides(n) {
  tutor_slideIndex = tutor_slideIndex + n;
  show_tutorial_slides(tutor_slideIndex);
}

// Thumbnail image controls
function tutor_currentSlide(n) {
  tutor_slideIndex = n;
  show_tutorial_slides(tutor_slideIndex);
}

function show_tutorial_slides(n) {
  var tutor_slides = document.getElementsByClassName("tutor_slides");
  var tutor_size = tutor_slides.length;

  if (n + 1 > tutor_size) {
    tutor_slideIndex = 0;
    n = 0;
  } else if (n < 0) {
    tutor_slideIndex = tutor_size - 1;
    n = tutor_size - 1;
  }

  for (i = 0; i < tutor_slides.length; i++) {
    tutor_slides[i].style.display = "none";
  }

  tutor_slides[n].style.display = "block";
}