import random

list = []

for i in range(0, 10):
    n = random.randint(1, 99)
    list.append(n)
print("queue is {}".format(list))

while len(list) != 0:
    currentNumber = list.pop(0)
    print("current Number is {} and the queue is {}".format(currentNumber, list))
print("the queue is now empty")