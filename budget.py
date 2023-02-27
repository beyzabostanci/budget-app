class Category:
  def __init__(self, name):
    self.ledger = []#to put results
    self.balance = 0 #for monney
    self.name = name #whos is this
    
  def deposit(self, amount, description= ""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += float(amount)

  def check_funds(self, amount):
    if amount >  self.balance:
      return False
    else:
      return True

  def get_balance(self):
    return self.balance
    #return sum(item["amount"] for item in self.ledger)

  def withdraw(self, amount, description= ""):
    if self.balance >= amount:
     self.ledger.append({'amount': -1 * amount, 'description': description})
     self.balance -= amount
     return True
    else: return False

  def transfer(self, amount, category):
    if self.check_funds(amount) == True:
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  def __repr__(self):
    line_width = 30
    stars = '*' * int((line_width - len(self.name)) / 2)
    string = stars + self.name + stars + '\n'
    for transaction in self.ledger:
        description = transaction['description'][:23]
        amount = f"{transaction['amount']:.2f}"[:7].rjust(int(line_width - len(description) - 1))
        string += f'{description} {amount}\n'
    string += f'Total: {self.str_balance()}'
    return string

  def str_balance(self):
      return f'{self.balance:.2f}'
"""
  def representation(self):
    header = self.name.center(30, "*") + "\n"
    ledger = ""
    for item in self.ledger:
      des = "{:<23}".format(item["description"])#first 23 characters
      amo = "{:7.2f}".format(item["amount"])#contain 2 decimal, max 7 characters
      ledger += "{}{}\n".format(des[:23], amo[:7])#put them side by side together
      total = "Total: {:.2f}".format(self.balance)#total result
    return header + ledger + total """
    
  
def create_spend_chart(categories):
   withdrawls = []
   for cat in categories:
    balance = 0
    for item in cat.ledger:
      if item['amount'] < 0:
        balance += abs(item['amount'])
    withdrawls.append(round(balance, 2))

   percent_spent = list(map(lambda amount: int((((amount/round(sum(withdrawls), 2)) * 10) // 1) * 10), withdrawls))
  
   chart_header = 'Percentage spent by category\n'
  
   chart_body = ''
   for value in range(100, -1, -10):
    chart_body += '{0}'.format(value).rjust(3) + '|'
    for percent in percent_spent:
      if percent >= value: chart_body += ' o '
      else: chart_body += '   '
    chart_body += ' \n'
  
   chart_footer = '    ' + '-' * ((3 * len(categories)) + 1) + '\n'
  
   descs = list(map(lambda cat: cat.name, categories))
   max_descs_length = max(map(lambda desc: len(desc), descs))
  
   upd_descs = list(map(lambda desc: desc.ljust(max_descs_length), descs))

   for x in zip(*upd_descs):
    chart_footer += '    ' + ''.join(map(lambda s: s.center(3), x)) + ' \n'

   return (chart_header + chart_body + chart_footer).rstrip('\n')
