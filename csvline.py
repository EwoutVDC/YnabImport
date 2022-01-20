from transaction import Transaction
from payee_info import regex_payee_category

from datetime import date

class InputException(Exception):
    pass

class IgnoreException(Exception):
    pass

class CsvLine:
    def __init__(self):
        self.amount = 0
        self.date = date.today()
    
    def GetMemo(self):
        return ""
    
    def ToTransaction(self):
        for l in regex_payee_category:
            if (l[0].search(self.GetMemo()) != None):
                if (l[1] == "#IGNORE#"):
                    raise IgnoreException("ignore '" + l[0].pattern + "'")
                return Transaction(self.date, l[1], l[2], self.GetMemo(), self.amount)
        return Transaction(self.date, "", "", self.GetMemo(), self.amount)
