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


# inheriting from the class Employee with all of it's functionality
class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())

emp_1 = Employee('Marcin', 'Brzeski', 60000)
emp_2 = Employee('test','user',50000)

# my_date = datetime.date(2016, 7, 10)
# print(Employee.is_workday(my_date))

dev_1 = Developer('Marcin','Brzeski',60000,'Python')

mgr = Manager('Marcin', 'Brzeski', 60000, [emp_2])

mgr.print_emps()