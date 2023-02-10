# while condition:
# code

# print a line 10 times
# i = 1
# while i < 10:
#     print("This is Line ")
#     i += 1


# print 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# print even number between 1 to 100
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# print even & Odd number between 1 to 100
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         print(str(i)+" Is Event")
#     else:
#         print(str(i) + " Is Odd")
#     i += 1

# print even & Odd between two number
fromStart = int(input("Enter Start Value:"))
toEnd = int(input("Enter End Value: "))
while fromStart <= toEnd:
    if int(fromStart) % 2 == 0:
        print(str(fromStart)+" Is Event")
    else:
        print(str(fromStart) + " Is Odd")
    fromStart += 1
