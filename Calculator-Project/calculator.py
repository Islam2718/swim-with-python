import CustomMessage
import OperationModule

CustomMessage.MyMessage("Welcome to Calculation using Python")

valueOne = int(input("Enter First Value: "))
action = input("Action: ")
valueTwo = int(input("Enter Second Value: "))

OperationModule.Operation(valueOne, action, valueTwo)
