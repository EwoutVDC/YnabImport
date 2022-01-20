# YnabImport
 Convert bank statement CSV files to ynab 4 import format

Add a file called "payee_info.py" that contains a list "regex_payee_category" with payee and category information and regexes to match for
eg:
regex_payee_category = [
    ["Example.*Payee", "Example Payee", ""],
    ["Example store", "StoreE", "Food"],
]

Add input files in a folder data/in and create a folder data/out
The file names are hardcoded into the code for every statement type
Just run the .py file for the type of statement you are trying to process.
