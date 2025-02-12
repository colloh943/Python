# arithmetic operators  (+,-,/,%,*)
from operator import truediv
from tokenize import endpats

a=23
b=14
total= a + b
print("the total is" ,total)
print(f'the total is  {total}')
subtract = a - b
print("the subtract is",subtract)
print(f'the subtract is  {subtract}')
multiply = a * b
print("the multiplication is", multiply)
print(f'the multiplication is  {multiply}')
divide = a / b
print("the division is", divide)
print(f'the division is  {divide}')
remainder = a % b
print("the remainder is", remainder)
print(f'the remainder is  {remainder}')
# comparison operators(==,>,<,>=,<=,!=)
age1 = 23
age2 = 12
print(f'Is age1 equal to age2 {age1 == age2}')
print(f'Is age1 greater than age2? {age1>age2}')
print(f'Is age1 less than age2? {age1<age2}')
print(f'Is age2 greater or equal to age1? {age2>=age1}')
print(f'Is age2 less or equal to age1? {age2<=age1}')
print(f'Is age2 not equal to  age1? {age2!=age1}')
# logical operators(and,or,not)
math =  67
science = 56
swahili = 78
french = 59
print(math>science and swahili>french)
print(math<science and swahili<french)
print(math>=science and swahili<=french)
print(math>science or swahili>french)
print(not(math<science or swahili<french))
print(not(math>=science or swahili<=french))


#
number1= input("enter a number" )
number2=input("enter a number")
number3=input("enter a number")
number4=input("enter a number")
number5=input("enter a number")
number6=input("enter a number")
number7=input("enter a number")
number8=input("enter a number")
divide1 = 'number1 / number2'
print("the division is", divide1)
divide2='number3/number4'
print("the division is", divide)
divide3='number5/number6'
print("the division is", divide)
divide4='number7/number8'
print("the division is", divide)
password=input("enter a password")
username= input("enter a username")
print(f'The username is {username}')
print(f'the password is {password}')
print(username == 'admin' and password == 'secure123')



code=float(input('Enter the code: '))
print((code>50) or (code<100))
if code>50 and code<100:
    print('true')
else:
    print('false')


