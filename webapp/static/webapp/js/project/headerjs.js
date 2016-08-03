var logincheck = 0;

<<<<<<< HEAD
function loginUpdate() {
  "use strict";
  $("#loginpending").toggle();
  $("#loggedin").toggle();
}

function launch() {
  "use strict";
  var loginpending = document.getElementById("loginpending").style.display;
  var loggedin = document.getElementById("loggedin").style.display;
  if (loginpending === "none") {
    logincheck = 0;
    loginUpdate();
  } else if (loggedin === "none") {
    logincheck = 1;
    loginUpdate();
  }
=======
function decision() {
    x += 1;
    if (x == 1) {
        $("mySidenav").css("width", "250px");
        $("main").css("margin-left", "250px");
        $("headername").toggle();
    } else {
        $("mySidenav").css("width", "0");
        $("main").css("margin-left", "0");
        $("headername").toggle();
        x -= 2;
    }
>>>>>>> b81b08d0088672a9bd06284172fee99147f9e30e
}
