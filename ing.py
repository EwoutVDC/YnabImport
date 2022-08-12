#!/usr/bin/env python3

from csvline import *
from process_files import process_files

from datetime import *
import re

class IngCsvLine(CsvLine):
    def __init__(self, line):
        print(line)
        values = line.split(';')
        if (values[4] == ""):
            raise InputException("no date")
        self.date = datetime.strptime(values[4], "%d/%m/%Y").date()
        self.amount = float(values[6].replace(',', '.'))
        if (self.amount == 0):
            raise InputException("amount 0")
        self.description = values[8]
        self.detail = values[9]

    def __str__(self):
        return str(self.date) + " - " + str(self.amount) + " - " + self.description + " - " + self.detail
    
    def GetMemo(self):
        memo = self.description
        if (self.detail):
            memo += ": " + self.detail
        return re.sub(",","",re.sub("\s\s+", " ", memo))

if __name__ == '__main__':
    process_files(IngCsvLine, "data/in/ing.csv", "data/out/ing_out.csv")
