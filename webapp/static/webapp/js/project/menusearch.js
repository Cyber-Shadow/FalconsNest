var changeVal, findItem, menulist, sumAmounts, updateItem;

menulist = [["Angus Beef Burger", 5], ["BLT Burger", 5], ["BLT Wrap", 5], ["Chicken Burger", 5], ["Chicken Schnitzel", 5], ["Dragon Burger", 5], ["Instant Noodles", 3.5], ["Sushi", 3.5], ["Bacon Roll", 4], ["Bacon & Egg Roll", 4.2], ["Butter Chicken & Rice", 5.5], ["Spaghetti", 6]];

sumAmounts = function() {
  var a;
  return ((function() {
    var m, ref, results;
    results = [];
    for (a = m = 0, ref = menulist.length - 1; 0 <= ref ? m <= ref : m >= ref; a = 0 <= ref ? ++m : --m) {
      results.push(menulist[a][2]);
    }
    return results;
  })()).reduce(function(a, b) {
    return a + b;
  });
};

findItem = function() {
  var amounts, costs, endresult, i, j, m, n, ref, ref1, temp, valcheck;
  valcheck = ($("#menuinput").val()).toLowerCase();
  endresult = [];
  costs = [];
  amounts = [];
  for (i = m = 0, ref = menulist.length - 1; 0 <= ref ? m <= ref : m >= ref; i = 0 <= ref ? ++m : --m) {
    if ((menulist[i][0].toLowerCase()).indexOf(valcheck) !== -1 && valcheck.length !== 0) {
      endresult.push(menulist[i][0]);
      costs.push(menulist[i][1]);
      amounts.push(menulist[i][2]);
    }
  }
  endresult = endresult.slice(0, 3);
  if (endresult.length !== 0) {
    for (j = n = 0, ref1 = endresult.length - 1; 0 <= ref1 ? n <= ref1 : n >= ref1; j = 0 <= ref1 ? ++n : --n) {
      temp = (endresult[j].split(" ")).join("_");
      endresult[j] = endresult[j] + " ($" + costs[j] + ")" + "<button class='btn flatbutton' id='" + temp + "minus' onClick='changeval(\"" + endresult[j] + "\", -1)'>-</button> <input class='itemamount' id='" + temp + "amount' value='" + amounts[j] + "' onkeyup='updateItem(\"" + endresult[j] + "\")'></input> <button class='btn flatbutton' id='" + temp + "plus' onClick='changeval(\"" + endresult[j] + "\", 1)'>+</button>";
    }
  }
  return $("#dropdownmenu").html(endresult.join("<br>"));
};

changeVal = function(string, amount) {
  var k, m, ref, results, sum;
  sum = sumAmounts();
  results = [];
  for (k = m = 0, ref = menulist.length - 1; 0 <= ref ? m <= ref : m >= ref; k = 0 <= ref ? ++m : --m) {
    if (string === menulist[k][0]) {
      if ((amount === -1 && menulist[k][2] === 0) || (amount === 1 && sum === 3)) {

      } else {
        menulist[k][2] += amount;
        results.push($("#" + (menulist[k][0].split(" ")).join("_") + "amount").val(menulist[k][2]));
      }
    } else {
      results.push(void 0);
    }
  }
  return results;
};

updateItem = function(string) {
  var amount_val, l, m, prev_sum, ref, results, sum;
  prev_sum = sumAmounts();
  amount_val = ($("#" + (string.split(" ")).join("_") + "amount").val()).replace(/\D/g, '');
  $("#" + (string.split(" ")).join("_") + "amount").val(amount_val);
  results = [];
  for (l = m = 0, ref = menulist.length - 1; 0 <= ref ? m <= ref : m >= ref; l = 0 <= ref ? ++m : --m) {
    if (string === menulist[l][0]) {
      menulist[l][2] = amount_val | 0;
      sum = sumAmounts();
      if (sum > 3) {
        $("#" + (menulist[l][0].split(" ")).join("_") + "amount").val(3 - prev_sum);
        results.push(menulist[l][2] = ($("#" + (menulist[l][0].split(" ")).join("_") + "amount").val()) | 0);
      } else {
        results.push(void 0);
      }
    } else {
      results.push(void 0);
    }
  }
  return results;
};
