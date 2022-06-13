number = int(input("Please guess a number: "))
print("Your guess is: {}".format(number))

while number != 30:
    number = int(input("Wrong\nPlease guess again: "))
else:
    print("Well done! Yes the number was 30")
