# x = int(input("Enter a number: "))
# y= x % 2
# print(y)
# if y == 1:
#     print("{} is an odd number".format(x))
# else:
#     print("{} is an even number".format(x))

# x = int(input("Enter a grade(%): "))
# while x < 0:
#     x = int(input("Enter a grade between 0 and 100(%): "))
# while x > 100:
#     x = int(input("Enter a grade between 0 and 100(%): "))

# if x >= 0 and x < 101:
#     if x <= 40:
#         print("Fail")
#     elif x <= 49:
#         print("Pass")
#     elif x <= 59:
#         print("Merit 2")
#     elif x <= 69:
#         print("Merit 1")
#     elif x <= 100:
#         print("Distinction")

# x = 0

# while x < 100:
#     x += 2
#     print(x)

import random
x = 30
# y = int(input("Enter a number: "))
y = random.randint(0, 100)
print(y)
while y != x:
    if y < 30:
        #print("guess too low")
        print("{} too low".format(y))
        #y = int(input("Please guess again: "))
        y = random.randint(0, 100)
    elif y > 30:
        #print("guess too high")
        print("{} too high".format(y))
        #y = int(input("Please guess again: "))
        y = random.randint(0, 100)


if y == x:
    print("Well done! Yes the number was 30")
