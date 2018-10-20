#!/usr/bin/env python3

import sys

try:
    salary = int(sys.argv[1])
    if salary <= 0:
        print("Paramenter Error")
        exit()
except:
    print("Paramenter Error")
    exit()

taxable_income = salary - 3500
if taxable_income > 80000:
    tax = taxable_income* 0.45 - 13505
elif taxable_income > 55000:
    tax = taxable_income * 0.35 - 5505
elif taxable_income > 35000:
    tax = taxable_income * 0.30 - 2755
elif taxable_income > 9000:
    tax = taxable_income * 0.25 - 1005
elif taxable_income > 4500:
    tax = taxable_income * 0.20 - 555
elif taxable_income > 1500:
    tax = taxable_income * 0.10 - 105
elif taxable_income > 0:
    tax = taxable_income * 0.03
else:
    tax = 0

print("{:.2f}".format(tax))
