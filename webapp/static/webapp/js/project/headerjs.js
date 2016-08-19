var menulist = [
  ["Falcon Burger", 5],
  ["BLT Wrap", 5],
  ["BLT Burger", 5],
  ["Expensive Thing", 100]
]

function find_item(input) {
  var endresult = []
  for (i = 0; i < menulist.length; i++) {
    if (input in menulist[i]) {
      endresult.push(menulist[i]);
    }
  }
  $("#dropdownmenu").html(endresult.join(""));
}
