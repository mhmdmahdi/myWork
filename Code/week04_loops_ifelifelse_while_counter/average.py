x = int(input("Enter a number: "))
print(x)
list = [x]


for x in list:
    x = int(input("Enter a number (0 to quit): "))
    print(list)
    if x != 0:
        list.append(x)

avg = sum(list) / len(list)
print("Average of list is {}".format(avg))
