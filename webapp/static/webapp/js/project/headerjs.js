var logincheck = 0;

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
}
