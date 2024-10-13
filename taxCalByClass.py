# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 22:57:16 2024

@author: USER
"""

class employee:
    def __init__(self,id=None, salary=None,department=None):
        self.id=id 
        self.salary=salary
        self.department=department
        
    def tax(self):
        return self.salary*0.3
    def netsalary(self):
        return self.salary - self.tax()
    
james=employee(int(input('enter an id:')),int(input('enter your salary:')))
print('tax to pay is:',james.tax())
print('remaining salary is:',james.netsalary())