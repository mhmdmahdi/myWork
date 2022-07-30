def displayMenu():
    print("What would you like to do?")
    print("\t (a) Add new student")
    print("\t (v) View students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q):")
    return choice
# def doAdd():
#     print("in adding")


def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter students name: ")
    students.append(currentStudent)

# def doView():
#     print("in viewing")


students = []
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
        choice = displayMenu()
        print(students)
    # elif choice == 'v':
    #     doView()
    elif choice != 'q':
        print("\n please select either a, v or q")
    elif choice == '':
        print(students)


print("you chose {}".format(choice()))
