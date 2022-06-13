import random

number = random.randint(1, 100)
print(number)

#number = int(input("Please guess a number: "))
#print("Your guess is: {}".format(number))

if number < 30:
    print("too low")
else:
    print("too high")

while number != 30:
    number = int(input("Wrong\nPlease guess again: "))
else:
    print("Well done! Yes the number was 30")
