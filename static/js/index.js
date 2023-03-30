let bg = document.getElementById("bg");
let moon = document.getElementById("moon");
let mountain = document.getElementById("mountain");
let road = document.getElementById("road");
let Title = document.getElementById("Title");

window.addEventListener("scroll", function () {
  let value = window.scrollY;

  bg.style.top = value * 0.5 + "px";
  moon.style.left = -value * 0.5 + "px";
  mountain.style.top = -value * 0.15 + "px";
  road.style.top = value * 0.15 + "px";
  Title.style.top = value * 1 + "px";
});
