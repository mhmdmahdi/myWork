# lists [] can be changed 'ie are mutable' ["This", "list", "contains", "dicts", "numbers", "strings", "and", "booleans", 123, True, {}]
# arrays are lists that must contain data types of the same element []: ["Meet", "Joe", "Bloggs"]
# lists need not contain elements of the same element
# tuples () cannot be changed 'ie are immutable': ("This", "tuple", "cannot", "be", "appended")
# dictionaries are lists that assign values to a key {}: {"Firstname": "Mohammed", "surname": "Mahdi"}
import array
import numpy

myList = ["String", 123, True, {}]
myArray1 = array.array('i', [1, 2, 3])
myArray2 = numpy.array([4, 5, 6])

myTuple = ("This", "tuple", "cannot", "be", "appended")

myList.append("Another String")
myArray1.append(4)
myArray3 = numpy.array(myArray1)
# numpy arrays cannot be appended but the array within can be appended and then integrated within a numpy array for better visualisation

print(myList)
print(myArray1)
print(myArray2)
print(myArray3)
print(myTuple)
