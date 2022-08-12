from payee_info import regex_payee_category #list of [ [regex as string, payee, category], ... ]
from csvline import *

from datetime import *
import re

for l in regex_payee_category:
    l[0] = re.compile(l[0])

def process_files(classname, inputfile, outputfile, linesToMerge=1):
    with open (inputfile) as f:
        lines = f.readlines()
        del lines[0]
        transactions = []
        exceptions = []
        linesMerged = 0
        mergedLine = ""
        for (i, line) in enumerate(lines, start=2):
            linesMerged += 1
            mergedLine += line.strip()
            if (linesMerged < linesToMerge):
                mergedLine += ";"
                continue
                 
            try:
                t = classname(mergedLine).ToTransaction()
                transactions.append(t)
                print (i, str(t))
            except InputException as err:
                print("InputException: " + str(err) + " For input: '" + mergedLine + "'")
            except IgnoreException as err:
                print("Exception: " + str(err) + " For input: '" + mergedLine + "'")
            except Exception as err:
                exceptions.append([i, err, mergedLine])
            
            linesMerged = 0
            mergedLine = ""
        
        if (len(exceptions) > 0):
            print ("\033[1;31;40mExceptions:\n\033[0;37;40m")
        for (i, err, line) in exceptions:
            print("\033[1;31;40mException at input line " + str(i) + ": " + str(err) + "\033[0;37;40m For input: '" + line + "'")
        
    with open (outputfile, "w") as f:
        f.write("Date,Payee,Category,Memo,Outflow,Inflow\n")
        for t in transactions:
            f.write(t.ynab_line() + "\n")

if __name__ == '__main__':
    print("Don't run this file. Run a .py file for the type of statement you are trying to process.")
