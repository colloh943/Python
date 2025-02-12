from Classes import Person
person1 = Person()
print(person1.first_name)
print(person1.last_name)
print(person1.age)
print(person1.gender

person2 = Person()
print(person2.first_name)
print(person2.last_name)
print(person2.age)
print(person2.gender)


from Classes import Emobilis_Employee, Developer, Teacher,Commission_Employee,Bank_Account

employee1 = Employee("John","Male",100000,25,"developer",1000)
employee2 = Employee("Jane","Female",40000,30,"nurse",200)
employee3 = Employee("Simon","Male",20000,20,"driver",100)
employee4 = Employee("Tom","Male",30000,19,"security",300)


print(employee1.basic_salary)
print(employee2.gender)
print(employee3.position)
print(employee4.tax_paid)
print(employee1.display())
print(employee2.display())
print(employee3.full_salary())
print(employee4.full_salary())
print(employee1.new_salary())
print(employee2.new_salary())
print(employee3.new_salary())


car1=Car("Volkswagen",2021,12356,9800000)
car2=Car("Benz",2023,3000,15000000)
car3=Car("toyota prado",2024,456186,4500000)


print(car1.model)
print(car2.milage)
print(car3.year)
print(car1.display())
print(car2.display())
print(car3.display())
print(car1.display())


rectangle1=Rectangle(5,10)
rectangle2=Rectangle(30,120)
rectangle3=Rectangle(300,2000)
rectangle4=Rectangle(250,1500)
rectangle5=Rectangle(1000,3000)


print(rectangle1.perimeter())
print(rectangle4.area())
print(rectangle2.display()



emobilis_employee1=Emobilis_Employee("Mary","Female",1500000,25,"Degree")
emobilis_employee2=Emobilis_Employee("Juma","Male",1800000,21,"Diploma")
emobilis_employee3=Emobilis_Employee("Mike","Male",2000000,40,"Masters")
developer1=Developer("collins","Male",1500000,25,"Degree","frontendDeveloper","python")
developer2=Developer("Betty","Female",2000000,18,"Diploma","backendDeveloper","HTML")

print(emobilis_employee1.qualification)
print(emobilis_employee2.salary)
print(emobilis_employee1.promotion())
print(emobilis_employee2.promotion())
print(emobilis_employee3.promotion())
print(developer1.specialization)
print(developer2.programing_language)


teacher1=Teacher("Jane","female",1500000,40,"Degree","5 years","deputy","sciences")
teacher2=Teacher("Tom","Male",20000,25,"Diploma","5 years","PE teacher","PE")
print(teacher1.specialization)
print(teacher2.position)






commission_employee1=Commission_Employee("Kibunja","Male",12300,34,"Degree",50,15)
commission_employee2=Commission_Employee("Adiel","Male",10000,34,"Degree",5000,17)

print(commission_employee1.Commission_salary())





user1=Bank_Account("Daisy",16,"children")
