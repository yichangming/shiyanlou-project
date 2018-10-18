#!/usr/bin/env python3

import sys

def salarywilltax(salary):
    return salary * (1 - 0.08 - 0.02 - 0.005 - 0.06)

def tax(taxable_income):
    taxable_income -= 3500
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
    return tax

def salaryaftertax(income):
    a = salarywilltax(income)
    return a - tax(a)

if __name__ == '__main__':
    try:
        for arg in sys.argv[1:]:
            key,value = arg.split(':')
            money = int(value)
            print("{0}:{1:.2f}".format(key,salaryaftertax(money)))
    except:
        print("Parameter Error")
