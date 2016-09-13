sumAmounts = ->
  (menulist[a][2] for a in [0..menulist.length - 1]).reduce (a, b) -> a + b

findItem = ->
  valcheck = ($("#menuinput").val()).toLowerCase()
  endresult = []
  costs = []
  amounts = []
  for i in [0..menulist.length - 1]
    if (menulist[i][0].toLowerCase()).indexOf(valcheck) != -1 and valcheck.length != 0
      endresult.push menulist[i][0]
      costs.push menulist[i][1]
      amounts.push menulist[i][2]
  endresult = endresult.slice 0, 3
  if endresult.length != 0
    for j in [0..endresult.length - 1]
      temp = (endresult[j].split(" ")).join("_")
      endresult[j] = endresult[j] + " ($" + costs[j] + ")" + 
                                    "<button class='btn flatbutton' id='" + 
                                    temp + "minus' onClick='changeval(\"" +
                                    endresult[j] + "\", -1)'>-</button>
                                    <input class='itemamount' id='" + 
                                    temp + "amount' value='" + amounts[j] +
                                    "' onkeyup='updateItem(\"" + endresult[j] +
                                    "\")'></input>
                                    <button class='btn flatbutton' id='" + 
                                    temp + "plus' onClick='changeval(\"" +
                                    endresult[j] + "\", 1)'>+</button>"
  $("#dropdownmenu").html endresult.join "<br>"
  
changeVal = (string, amount) ->
  sum = sumAmounts()
  for k in [0..menulist.length - 1]
    if string == menulist[k][0]
      if (amount == -1 and menulist[k][2] == 0) or (amount == 1 and sum == 3)
      else
        menulist[k][2] += amount
        $("#" + (menulist[k][0].split(" ")).join("_") + "amount").val menulist[k][2]
        
updateItem = (string) ->
  prev_sum = sumAmounts()
  amount_val = ($("#" + (string.split(" ")).join("_") + "amount").val()).replace(/\D/g,'')
  $("#" + (string.split(" ")).join("_") + "amount").val amount_val
  for l in [0..menulist.length - 1]
    if string == menulist[l][0]
      menulist[l][2] = amount_val | 0
      sum = sumAmounts()
      if sum > 3
        $("#" + (menulist[l][0].split(" ")).join("_") + "amount").val 3 - prev_sum
        menulist[l][2] = ($("#" + (menulist[l][0].split(" ")).join("_") + "amount").val()) | 0
      