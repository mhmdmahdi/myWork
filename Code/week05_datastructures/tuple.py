#months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
#summer = months[4:7]
# for month in summer:
#    print(month)

# import random
# queue = []
# numberOfNumbers = 10
# rangeTo = 100

# for i in range(0, numberOfNumbers):
#     queue.append(random.randint(0,rangeTo))
# print("queue is {}".format(queue))

# while len(queue) != 0:
#     currentNumber = queue.pop(0)
#     print("current Number is {} and the queue is {} ".format(currentNumber, queue))

# print("the queue is now empty")

student = {
    "name": "Mary",
    "courses": [{"courseName": "Programming", "grade": 45},
                {"courseName": "History", "grade": 99}]
}
print("student: {}".format(student["name"]))
for i in student["courses"]:
    print("\t {} \t: {}".format(i["courseName"], i["grade"]))
