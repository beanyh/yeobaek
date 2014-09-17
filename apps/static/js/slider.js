if (navigator.msMaxTouchPoints) {
  $('#slider').addClass('ms-touch');
}

$('#slider').on('scroll', function() {
    $('.slide-image').css('transform','translate3d(-' + (100-$(this).scrollLeft()/6) + 'px,0,0)');
  });
}
else {
  var slider = {

    // The elements.
    el: {
      slider: $("#slider"),
      holder: $(".holder"),
      imgSlide: $(".slide-image")
    },

    // The stuff that makes the slider work.
    slideWidth: $('#slider').width(), // Calculate the slider width.

    // Define these as global variables so we can use them across the entire script.
    touchstartx: undefined,
    touchmovex: undefined, 
    movex: undefined,
    index: 0,
    longTouch: undefined,
    // etc

     init: function() {
      this.bindUIEvents();
    },

    bindUIEvents: function() {

      this.el.holder.on("touchstart", function(event) {
        slider.start(event);
      });

      this.el.holder.on("touchmove", function(event) {
        slider.move(event);
      });

      this.el.holder.on("touchend", function(event) {
        slider.end(event);
      });

    },




this.longTouch = false;
setTimeout(function() {
  // Since the root of setTimout is window we can’t reference this. That’s why this variable says window.slider in front of it.
  window.slider.longTouch = true;
}, 250);

$('.animate').removeClass('animate');


this.touchstartx =  event.originalEvent.touches[0].pageX;

this.movex = this.index*this.slideWidth + (this.touchstartx - this.touchmovex);

var panx = 100-this.movex/6;

if (this.movex < 600) { // Makes the holder stop moving when there is no more content.
  this.el.holder.css('transform','translate3d(-' + this.movex + 'px,0,0)');
}
if (panx < 100) { // Corrects an edge-case problem where the background image moves without the container moving.
  this.el.imgSlide.css('transform','translate3d(-' + panx + 'px,0,0)');
 }

 var absMove = Math.abs(this.index*this.slideWidth - this.movex);

 if (absMove > this.slideWidth/2 || this.longTouch === false) {
  if (this.movex > this.index*this.slideWidth && this.index < 2) {
    this.index++;
  } else if (this.movex < this.index*this.slideWidth && this.index > 0) {
    this.index--;
  }
}

// Move and animate the elements.
this.el.holder.addClass('animate').css('transform', 'translate3d(-' + this.index*this.slideWidth + 'px,0,0)');
this.el.imgSlide.addClass('animate').css('transform', 'translate3d(-' + 100-this.index*50 + 'px,0,0)');







