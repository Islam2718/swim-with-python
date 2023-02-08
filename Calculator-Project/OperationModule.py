def Operation(a, action, c):
    if (action == "+"):
        Addition(a, c)
    elif (action == "-"):
        Substraction(a, c)
    elif (action == "*"):
        Multiplication(a, c)
    elif (action == "/"):
        Division(a, c)
    elif (action == "compare"):
        GreaterTest(a, c)
    else:
        print("Do Nothing...")


def Addition(a, b):
    print(a+b)


def Substraction(a, b):
    print(a-b)


def Multiplication(a, b):
    print(a*b)


def Division(a, b):
    print(a/b)


def GreaterTest(a, b):
    if (a > b):
        print("Your First Value")
        print(a)
        print("is Greater than Second Value ")
        print(b)
    else:
        print("Your Second Value")
        print(b)
        print("is Greater than First Value ")
        print(a)
