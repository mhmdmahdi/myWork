string = input("enter a string: ")
lengthOfString = len(string)
print("The length of {} is {}".format(string, lengthOfString)) 

message = 'John said\t"hi"\nI said\t\t"bye"'
print(message)

rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print("That String normalised is :{}".format(normalisedString))
print("we reduced the input string from {} to {} characters".format(lenghtOfRawString, lenghtOfNormalised))
