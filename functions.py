def my_function():
    print("Hello World")
    print("Hello World")
my_function()
my_function()
my_function()



def my_function2():
    salute= "Hello World"
    print(salute)

my_function2()
my_function2()




def customers(salute):
    print(salute)
customers("Hello World")
customers("Hello James")
customers("ANYTHING")
customers("Hello Collins")



def employees(first_name, last_name,age):
    print(f'Hello {first_name}{last_name}   and you are {age}years old')
employees("Hillary", "Smith",13)
employees("Harrun", "kipngetich",16)
employees("Sammy","Omondi",17)
employees("Nato","wambui",19)
employees("Harrun", "Smith",24)
employees("Kiptum", "Mercy",18)


def summation(first_number, second_number):
        addition = first_number + second_number
        subtraction = first_number - second_number
        print(f'the addition is: {addition}')
        print (f'the subtraction is: {subtraction} ')
summation(100,200)
summation(300,700)
summation(1345,565)

def multipler(first_number, second_number):
        product = first_number * second_number
        total =first_number+second_number
        return (f'the product is{product} and the totlal is{total}')
print(multipler( 5,5))
print(multipler(7586,345))

def age_calculator(current_age):
    new_age=current_age+36
    return new_age
print(age_calculator(18))


def bet_bonus(name,correct_score):
    if correct_score>=9 and correct_score<=13:
        return(f'{name} your bonus 5000')
    elif correct_score>=6 and correct_score<=9:
        return(f'{name} your bonus 3000')
    elif correct_score>=4 and correct_score<=6:
        return(f'{name} your bonus 2000')
    else:
        return(f'{name} your bonus 0')

print(bet_bonus("Paul",8))
print(bet_bonus("Marry",3))
print(bet_bonus("June",5))
print(bet_bonus("Kim",13))
print(bet_bonus("Godo",2))


def greet(name):
    if name=="Alice":
        return f'Hello {name} '
    elif name=="Bob":
        return f'Hello {name} '
    else:
        return f'Hello'
print(greet("Alice"))
print(greet("Bob"))
print(greet("james"))
print(greet("Alice"))
print(greet("COLLOH"))
print(greet("Harrun"))