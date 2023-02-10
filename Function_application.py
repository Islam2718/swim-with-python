# define a function to add two number
def sum(a, b):
    print(a+b)


# define a function to sub two number
def sub(a, b):
    print(a-b)


# define a function to mul two number
def mul(a, b):
    print(a*b)


# define a function to add div number
def div(a, b):
    print(a/b)


# calling function
firstValue = int(input("Enter Value1 = "))
secondValue = int(input("Enter Value2 = "))
actionValue = input("Action- ( +, -, x, /)? = ")

if actionValue == "+":
    sum(firstValue, secondValue)
elif actionValue == "-":
    sub(firstValue, secondValue)
elif actionValue == "x":
    mul(firstValue, secondValue)
elif actionValue == "/":
    div(firstValue, secondValue)
else:
    print("Invalid Input!")
