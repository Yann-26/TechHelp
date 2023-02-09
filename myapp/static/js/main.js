(function ($) {
    "use strict";

    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 40) {
            $('.navbar').addClass('sticky-top');
        } else {
            $('.navbar').removeClass('sticky-top');
        }
    });
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
    });
    
})(jQuery);

 
// SCRIPT DU COOKIE
window.onload = function() {
    var cookiePopup = document.getElementById("cookiePopup");
    var declineCookie = document.getElementById("declineCookie");
    var acceptCookie = document.getElementById("acceptCookie");
    
    // Vérifiez si l'utilisateur a déjà fait un choix en matière de cookies
    if (localStorage.getItem("cookieChoice") !== "accepted") {
      checkCookie();
    }
    
    declineCookie.addEventListener("click", function() {
      cookiePopup.classList.add("hide");
      localStorage.setItem("cookieChoice", "declined");
    });
    
    acceptCookie.addEventListener("click", function() {
      //Create date object
      let d = new Date();
      //Increment the current time by 1 minute (cookie will expire after 1 minute)
      d.setMinutes(2 + d.getMinutes());
      //Create Cookie withname = myCookieName, value = thisIsMyCookie and expiry time=1 minute
      document.cookie = "myCookieName=thisIsMyCookie; expires = " + d + ";";
      //Hide the popup
      cookiePopup.classList.add("hide");
      cookiePopup.classList.remove("show");
      localStorage.setItem("cookieChoice", "accepted");
    });
  };
  
  //Check if cookie is already present
  const checkCookie = () => {
    //Read the cookie and split on "="
    let input = document.cookie.split("=");
    //Check for our cookie
    if (input[0] == "myCookieName") {
      //Hide the popup
      cookiePopup.classList.add("hide");
      cookiePopup.classList.remove("show");
    } else {
      // Show the popup
      cookiePopup.classList.add("show");
      cookiePopup.classList.remove("hide");
    }
    //When user clicks the accept button
document.getElementById("acceptCookie").addEventListener("click", () => {
  //Create date object
  let d = new Date();
  //Increment the current time by 1 minute (cookie will expire after 1 minute)
  d.setMinutes(2 + d.getMinutes());
  //Create Cookie withname = myCookieName, value = thisIsMyCookie and expiry time=1 minute
  document.cookie = "myCookieName=thisIsMyCookie; expires = " + d + ";";
  //Hide the popup
  popUp.classList.add("hide");
  popUp.classList.remove("show");

  //Send a request to your API to store the choice in your database
  let xhr = new XMLHttpRequest();
  xhr.open("POST", "/api/store-cookie-choice");
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({ choice: "accepted" }));
});

//When user clicks the decline button
document.getElementById("declineCookie").addEventListener("click", () => {
  //Hide the popup
  popUp.classList.add("hide");
  popUp.classList.remove("show");

  //Send a request to your API to store the choice in your database
  let xhr = new XMLHttpRequest();
  xhr.open("POST", "/api/store-cookie-choice");
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({ choice: "declined" }));
});


  };
  