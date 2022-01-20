#!/usr/bin/env python3

from csvline import *
from process_files import process_files

from datetime import *

class SodexoCsvLine(CsvLine):
    def __init__(self, line):
        print(line)
        values = line.split(';')
        self.date = datetime.strptime(values[0], "%d-%m-%Y").date()
        self.amount = float(values[2].replace('"+ ', '').replace('"- ', '-').split(' ')[0])
        if (self.amount == 0):
            raise InputException("amount 0")
        self.memo = values[1]

    def __str__(self):
        return str(self.date) + " - " + str(self.amount) + " - " + self.GetMemo()
    
    def GetMemo(self):
        return self.memo

if __name__ == '__main__':
    process_files(SodexoCsvLine, "data/in/sodexo.csv", "data/out/sodexo_out.csv")
