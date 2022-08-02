import random
x = []

#print("random number: {}".format(numbers))

for i in range(0, 10):
    x.append(random.randint(0, 100))
print("list is {}".format(x))

topOnes = x.copy()
topOnes.sort(reverse=True)
print("The top {} are \t\t {}".format(3, topOnes[0:3]))
