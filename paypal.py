#!/usr/bin/env python3

from csvline import *
from process_files import process_files

from datetime import *

class PayPalCsvLine(CsvLine):
    def __init__(self, line):
        print(line)
        values = line.split('","')
        if (values[4] == 'General Authorization'):
            raise InputException("Ignore paypal general authorization")
        self.date = datetime.strptime(values[0].replace('"', ''), "%d/%m/%Y").date()
        self.amount = float(values[7].replace(',', '.'))
        if (self.amount == 0):
            raise InputException("amount 0")
        self.name = values[3]
        self.type = values[4]

    def __str__(self):
        return str(self.date) + " - " + str(self.amount) + " - " + self.GetMemo()
    
    def GetMemo(self):
        return self.name + " type: " + self.type

if __name__ == '__main__':
    process_files(PayPalCsvLine, "data/in/paypal.CSV", "data/out/paypal_out.csv")
