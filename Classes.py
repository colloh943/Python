class Person:
    first_name = "Alex"
    last_name =  "kinyanjiu"
    gender = "male"
    age = 18

class Employee:
    def __init__(self,name,gender,basic_salary,age,position,tax_paid):
        self.name = name
        self.gender = gender
        self.basic_salary = basic_salary
        self.age = age
        self.position = position
        self.tax_paid = tax_paid
    def display(self):
        return  f"name{self.name}   gender{self.gender} "
    def full_salary(self):
        return self.basic_salary + self.tax_paid +25000
    def new_salary(self):
        return self.basic_salary + self.basic_salary*0.27

class Car:
    def __init__(self,model,year,milage,price):
        self.model = model
        self.year = year
        self.milage = milage
        self.price = price
    def display(self):
        return f"model{self.model} year{self.year} milage{self.milage} price{self.price}"

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def perimeter(self):
        return (self.width +self.length) * 2
    def area(self):
        return self.width * self.length
    def display(self):
        return f"width{self.width} length{self.length}  "


class Emobilis_Employee():
    def __init__(self,name,gender,salary,age,qualification):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.age = age
        self.qualification = qualification

    def promotion(self):
        if self.qualification == "Degree" or self.qualification == "Masters" :
            return "you are promoted"
        else:
            return "you are not promoted"


class Developer(Emobilis_Employee):
    def __init__(self,name,gender,salary,age,qualification,specialization,programing_language):
        super().__init__(name,gender,salary,age,qualification)
        self.specialization = specialization
        self.programing_language = programing_language

class Teacher(Emobilis_Employee):
    def __init__(self,name,gender,salary,age,qualification,duration_of_service,position,specialization):
        super().__init__(name,gender,salary,age,qualification)
        self.duration_of_service = duration_of_service
        self.position = position
        self.specialization = specialization


class Commission_Employee(Emobilis_Employee):
    def __init__(self,name,gender,salary,age,qualification,commission_rate,hours_worked):
        super().__init__(name,gender,salary,age,qualification)
        self.commission_rate = commission_rate
        self.hours_worked = hours_worked

    def Commission_salary(self):
        commission_salary = (self.commission_rate * self.hours_worked)+ self.salary
        return commission_salary



class Bank_Account:
    def __init__(self,name,age,account_type,account_balance):
        self.name = name
        self.age = age
        self.account_type = account_type
        self.account_balance = account_balance
    def deposit (self):
        input("enter deposit amount" )
    def withdraw_Amount(self):
        input("enter withdraw amount" )
    def account_fee(self):
        account_fee = account_balance *0.5
        return self.account_fee
    def display(self):
        return self.account_balance , self.deposits , self.withdraw_amount

