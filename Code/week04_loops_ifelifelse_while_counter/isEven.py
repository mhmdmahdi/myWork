number = int(input("Enter a number: "))
print(number)

x = number % 2
print(x)

if x == 0:
    print("number is even")
else:
    print("number is odd")