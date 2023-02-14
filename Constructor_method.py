# OOP - constructor mehtod

class myClass:
    def __init__(self, name, message):
        print("construction method: ", message, "-", name)

    # def __init__(self):
    #     print("construction method")

    def myFunc1():
        print("this is my func1")

    def myFunc2():
        print("this is my func2")


# myclass = myClass()
myclass = myClass("Abdur Rahman", "Hello")
