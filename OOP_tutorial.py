# Python Object-Oriented Programming
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

import datetime

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    # initialization
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first,last,pay)

    # static method is not accessing any data from class/instance
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 5:
            return False
        return True


emp_1 = Employee('Marcin','Brzeski',60000)
emp_2 = Employee('test','user',50000)

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))