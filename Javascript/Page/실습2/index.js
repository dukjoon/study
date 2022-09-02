// 2) Image Slider

var slider = document.querySelector("#slider");
var slides = slider.querySelector(".slides");
var slide = slides.querySelectorAll(".slide");

var currentSlide = 0; //현재 화면에 보여지는 슬라이드

setInterval(function() {
    var from = -(1024 * currentSlide);  //현재 위치에서 어디로 이동할지
    var to = from - 1024; //'어디로'
    slides.animate({
        marginLeft: [from + "px", to + "px"]
    }, {
        duration: 500,
        easing: "ease",
        iterations: 1,
        fill: "both"
    });
    currentSlide++;
    if (currentSlide === (slide.length - 1)) {
        currentSlide = 0;   //마지막 슬라이드로 갔을 때 다시 처음으로
    }
}, 3000);