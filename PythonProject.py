# Write your code here
earned_amounts = {
  "Bubblegum": "$202",
  "Toffee": "$118",
  "Ice cream": "$2250",
  "Milk chocolate": "$1680",
  "Doughnut": "$1075",
  "Pancake": "$80"
}

print("Earned amount: ")

#Iterate through dictionary and add to variable total
total = 0

for x in earned_amounts.values():
  numeric_x = x.replace("$", "")
  total += int(numeric_x)
    
#Print multiline table of amounts
print("""Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80""")
    
#Print variable total + string for Income
print("Income: $"+str(total))

#Print other values
staff_expenses = int(input("Staff expenses: \n"))
other_expenses = int(input("Other expenses: \n"))
print(staff_expenses)
print(other_expenses)
net_income = total - (staff_expenses + other_expenses)
print("Net income: "+str(net_income))
