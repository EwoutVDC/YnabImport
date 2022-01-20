#!/usr/bin/env python3

from csvline import *
from process_files import process_files

from datetime import *

class KbcCsvLine(CsvLine):
    def __init__(self, line):
        print(line)
        values = line.split(';')
        self.date = datetime.strptime(values[5], "%d/%m/%Y").date()
        self.amount = float(values[8].replace(',', '.'))
        if (self.amount == 0):
            raise InputException("amount 0")
        self.memo = values[6]

    def __str__(self):
        return str(self.date) + " - " + str(self.amount) + " - " + self.GetMemo()
    
    def GetMemo(self):
        return self.memo

if __name__ == '__main__':
    process_files(KbcCsvLine, "data/in/kbc.csv", "data/out/kbc_out.csv")
