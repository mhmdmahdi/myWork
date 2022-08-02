# name = input("Hello. What is your name: ")
# surname = input("What is your surname: ")
# print("Your name is: {} {}".format(name, surname))

# i = 3
# float = 3.5
# bool = True
# str = "how now Brown Cow"
# list = []

# print("variable {} is of type: {} and value: {}".format('i', type(i), i))
# print("variable {} is of type: {} and value: {}".format('float', type(float), float))
# print("variable {} is of type: {} and value: {}".format('bool', type(bool), bool))
# print("variable {} is of type: {} and value: {}".format('str', type(str), str))
# print("variable {} is of type: {} and value: {}".format('list', type(list), list))

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = x-y
# print("{} minus {} is {}".format(x, y, z))

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = (x // y)
# remainder = x%y
# print("{} divided {} is {} with remainder {}".format(x, y, z, remainder))

# import random

# num = random.randint(1, 10)
# print(num)

# import math
# fl = float(input("Enter a float number: "))
# rounded = round(fl)
# print("{} rounded is {}".format(fl, rounded))

# val = float(input("Enter a number: "))
# val2 = abs(val)
# print("The absolute value of {} is {}".format(val, val2))

# import math
# num = float(input("Enter a float: "))
# down = math.floor(num)
# print("number {} rounded down is: {}".format(num, down))

# str = input("Please enter a string: ")
# length = len(str)
# print("The length of {} is {} characters".format(str, length))

# print('John said \t"hi"\nI said \t\t"bye"')

str = input("Please enter a string: ")
length = len(str)
normalised = str.strip().lower()
length2 = len(normalised)
print("str normalised is {}".format(normalised))
print("length reduced from {} to {}".format(length, length2))