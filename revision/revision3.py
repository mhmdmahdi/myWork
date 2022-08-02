x = int(input("Enter a number: "))
y = []

while x != 0:
    y.append(x)
    print(y)
    for x in y:
        x = int(input("Enter a number: "))
        y.append(x)
        print(y)
        if x == 0:
            avg = sum(y) / (len(y)-1)
            print("average is: {}".format(avg))

