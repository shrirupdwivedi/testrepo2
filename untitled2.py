#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 12:33:43 2022

@author: shrirupdwivedi
"""


        
class BankAccount():
    
    def __init__(self,balance=0):
        self.balance=balance
        
    def withdrawl(self,amount):
        if amount<1:
            raise ValueError('Amount should be positive')
        self.balance=self.balance-amount
        
    def deposit(self,amount):
        if amount<1:
            raise ValueError('Amount should be positive')
        self.balance+=amount




class SavingsAccount(BankAccount)
    
    def __init__(self,balance,interestrate):
        self.intrate=interestrate
    
    def interest(self,n_periods=1):
        
        return print(self.balance * ( (1+self.intrate)**n_periods -1 ))




class Customer(BankAccount):
    
    def __init__(self,f_name,l_name,addr,phone,accno):
        if (type(f_name) == str and type(l_name) == str and type(addr) == int and type(phone) == int):
            self.f_name=f_name
            self.l_name=l_name
            self.addr=addr
            self.phone=phone
            self.acc=accno
        else:
            raise TypeError('Inappropriate Data Type of one of more arguments')
        


        

    
class Employees:
    
    def __init__(self, empID,name,department,salary):
        self.empID=empID
        self.name=name
        self.department=department
        self.salary=salary
        print('ran')
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary<0:
            raise ValueError('Invalid Salary')
        else:
            self._salary=salary


    
        
    
        
    
    