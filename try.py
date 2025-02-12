from decimal import FloatOperation

number=float(input("Enter a number: "))
if number / 3 == True and number / 5 == True:
    print ("FuzzBuzz")

elif (number/5 == True):
    print("Fuzz")
elif (number/3 == True):
    print("Buzz")
else:
    print(number)


number= input("Enter a number: ")
if (number/3) and (number/5):
    print("FuzzBuzz")
elif (num/3):
    print("Fuzz")
elif (num/5):
    print("Buzz")
else:
    print(num)


withdraw_amount=input("Enter your withdrawal amount: ")
if withdraw_amount <=100 :
    print("charges =0")
else:
    charges=withdraw_amount+10/100
    print("charges =",charges)














