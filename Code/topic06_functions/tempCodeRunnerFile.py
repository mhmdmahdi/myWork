
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
    # elif choice == 'v':
    #     doView()
    elif choice != 'q':
        print("\n please select either a, v or q")
    choice = displayMenu()
    
print("you chose {}".format(choice()))