#!/usr/bin/env python3

import sys
import csv
import args
import userdata
import config
from multiprocessing import Process, Queue, Pool

class IncomeTaxCalculator(object):

    def __init__(self, config, userinfo,outfile):
        self.outfile = outfile
        self.config = config
        self.userinfo = userinfo
        self.outfile = outfile
        self.salaryinfo = []
        self.queue1 = Queue()
        self.queue2 = Queue()

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

    def calc_for_all_userdata(self,q1,q2):
        while True:
            try:
                user = q1.get(timeout=0.1)
            except:
                print('queue is null,exit')
                return
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
            #salaryinfo.append([user_id,user_salary,tax1,tax2,salaryaftertax])
            #self.salaryinfo[user_id] = {'salary':user_salary,'shebao':tax1,'tax':tax2, 'aftertax':salaryaftertax}
            print(salaryaftertax)
            q2.put([user_id,user_salary,tax1,tax2,salaryaftertax])

    def multiprocess_calc(self):
        p1=Process(target = self.userinfo._read_file, args=(self.queue1,))
        p2=Process(target = self.calc_for_all_userdata, args=(self.queue1,self.queue2))
        p3=Process(target = self.export, args=(self.queue2,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        print("end")

    def export(self,queue):
        with open(self.outfile, 'w') as f:
            writer = csv.writer(f)
            while True:
                try:
                    data = queue.get(timeout=0.2)
                except:
                     break 
                writer.writerow(data)

if __name__ == '__main__':
    _arg = args.Args(sys.argv[1:])
    configfile = _arg.get_arg('config')
    config = config.Config(configfile)
    userdatafile = _arg.get_arg('userdata')
    userinfo = userdata.UserData(userdatafile)
    outfile = _arg.get_arg('out')
    income = IncomeTaxCalculator(config,userinfo,outfile)
    income.multiprocess_calc()
    #print(income.salaryinfo)
    #income.export()
