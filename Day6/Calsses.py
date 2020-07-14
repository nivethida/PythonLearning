# -*- coding: utf-8 -*-

import statistics
class Employee:
    
    raise_amount = 100000
    
    def __init__(self, f_name, l_name, salary):
        self.last_name = l_name
        self.first_name = f_name
        self.pay = salary
        self.email = f_name+"."+l_name+"@csueastbay.edu"
        
    def get_email1(self):
        print(self.email)
    
    def get_email2(self):
        return self.email
        
    def fullName(self):
        return '{}, {}'.format(self.last_name, self.first_name)
    
    def raise_pay(self):
        self.pay += Employee.raise_amount       
    
    def bonus(self, revenue):
        theBonus = 0.1*revenue
        self.bonus = theBonus
    
    def performance(self, *revenue):
        print(revenue)
        print(statistics.mean(revenue))
        
        

employee1 = Employee("x", "y",50000)  
employee2 = Employee("s", "t",60000)      

print(employee1.email)
print(employee2.email)

print(employee2.get_email2)

employee2.get_email1()

employee2.raise_pay()

print(employee2.pay)

employee1.bonus(2000000)
print(employee1.bonus)

employee1.performance(10000,20000,22200,40000)

Employee.performance(employee1, 10000,20000,30000,40000)






























