x = 0;

function decision() {
    x += 1;
    if (x == 1) {
        $("mySidenav").css("width", "250px");
        $("main").css("marginLeft", "250px");
        $("headername").toggle();
    } else {
        $("mySidenav").css("width", "0");
        $("main").css("marginLeft", "0");
        $("headername").toggle();
        x -= 2;
    }
}
