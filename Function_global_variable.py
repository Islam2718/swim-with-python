# Function with global variable

# global variable declaration
wish = "Good Day"
number = 5
# define function


def myMessage():
    # print(wish)
    # print(number+2) | arithmatic operation allowed

    # modification of global var not alowed but we can declare the var as global
    # global number bad practice
    myvalue = number
    myvalue = 10
    print(myvalue)


# function calling
myMessage()
