import math
class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    result = self.name.center(30, "*") + "\n"
     
    for item in self.ledger:
      result += item["description"][:23] + ("{:.2f}".format(round(item["amount"], 2))).rjust(30-len(item["description"][:23])) + "\n"

    result += "Total: " + str(self.get_balance())
      
    return result
  
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount" : amount, "description" : description})

  def withdraw(self, amount, description = ""):
    if (self.check_funds(amount)):
      self.deposit(-amount, description)
      return True
    return False
    
  def get_balance(self):
    return sum([item['amount'] for item in self.ledger])

  def transfer(self, amount, budget):
    if (self.get_balance() < amount):
      return False
    self.withdraw(amount, f"Transfer to {budget.name}")
    budget.deposit(amount, f"Transfer from {self.name}")
    return True

  def check_funds(self, amount):
    return self.get_balance() >= amount


def create_spend_chart(categories):
  result = "Percentage spent by category\n"

  withdrawals_amounts = []
  
  for category in categories:
    withdrawals_amount = 0;
    for item in category.ledger:
      if item["amount"] < 0:
        withdrawals_amount += item["amount"]
    withdrawals_amounts.append(-withdrawals_amount)

  withdrawals_sum = sum(withdrawals_amounts)

  withdrawals_ratios = []
  for category in withdrawals_amounts:
    withdrawals_ratios.append(math.floor( (category * 100 // withdrawals_sum) /10) *10)

  for i in range(100, -1, -10):
    result += str(i).rjust(3) + "|"
    for category in withdrawals_ratios:
      if category >= i:
        result += " o "
      else:
        result += "   "
    result += " \n"

  result += "    " + "---"*len(withdrawals_ratios) + "-"

  longest_name = ""
  for category in categories:
    if len(category.name) > len(longest_name):
      longest_name = category.name
  
  for i in range(len(longest_name)):
    result += "\n    "
    for j in range(len(categories)):
      if (len(categories[j].name) <= i):
        result += "   "
      else:
        result += " " + categories[j].name[i] + " "
    result += " "
      
  return result
