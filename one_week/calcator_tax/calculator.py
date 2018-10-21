#!/usr/bin/env python3

import sys
import csv
import args
import userdata
import config

class IncomeTaxCalculator(object):

    def __init__(self, config, userinfo,outfile):
        self.outfile = outfile
        self.config = config
        self.userinfo = userinfo
        self.outfile = outfile
        self.salaryinfo = []

    def incometax(self, salary):
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
        return tax

    def calc_for_all_userdata(self):
        for user in self.userinfo.get_users():
            user_id,user_salary_str = user
            user_salary = int(user_salary_str)
            ratio = self.config.get_tax_rate()
            if user_salary < self.config.get_jishuL():
                tax_jishu = sauserself.config.get_jishuL()
            elif user_salary > self.config.get_jishuH():
                tax_jishu = self.config.get_jishuH()
            else:
                tax_jishu = user_salary
            tax1 = float('%.2f'%(tax_jishu * ratio))
            tax2 = float('%.2f'% self.incometax(user_salary-tax1))
            salaryaftertax = float('%.2f'% (user_salary - tax1 - tax2))
            self.salaryinfo.append([user_id,user_salary,tax1,tax2,salaryaftertax])
            #self.salaryinfo[user_id] = {'salary':user_salary,'shebao':tax1,'tax':tax2, 'aftertax':salaryaftertax}

    def export(self):
        with open(self.outfile, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(self.salaryinfo)

if __name__ == '__main__':
    _arg = args.Args(sys.argv[1:])
    configfile = _arg.get_arg('config')
    config = config.Config(configfile)
    userdatafile = _arg.get_arg('userdata')
    userinfo = userdata.UserData(userdatafile)
    outfile = _arg.get_arg('out')
    income = IncomeTaxCalculator(config,userinfo,outfile)
    income.calc_for_all_userdata()
    print(income.salaryinfo)
    income.export()
