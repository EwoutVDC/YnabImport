from datetime import date

class Transaction:
    def __init__(self, date, payee, category, memo, amount):
        self.date = date
        self.payee = payee
        self.memo = memo
        self.amount = amount
        self.category = category
    
    def ynab_line(self):
        if (self.amount == 0):
            raise Exception("amount 0")
        line = self.date.strftime("%d/%m/%Y") + ","  + self.payee + "," + self.category + "," + self.memo.replace(',', ';') + ","
        if (self.amount < 0):
            line += str(abs(self.amount)) + ","
        else:
            line += "," + str(self.amount)
        return line
    
    def __str__(self):
        return self.ynab_line()
