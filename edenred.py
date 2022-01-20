#!/usr/bin/env python3

from csvline import *
from process_files import process_files

from datetime import *

class EdenredCsvLine(CsvLine):
    def __init__(self, line):
        print(line)
        values = line.split('\t')
        self.date = datetime.strptime(values[0], "%d/%m/%Y %H:%M").date()
        self.amount = float(values[4].replace('+ ', '').replace(',', '.').split(' ')[0])
        if (self.amount == 0):
            raise InputException("amount 0")
        self.memo = values[1]

    def __str__(self):
        return str(self.date) + " - " + str(self.amount) + " - " + self.GetMemo()
    
    def GetMemo(self):
        return self.memo

if __name__ == '__main__':
    process_files(EdenredCsvLine, "data/in/edenred.csv", "data/out/edenred_out.csv")
