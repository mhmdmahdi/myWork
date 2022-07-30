import random
import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

print(salaries)

plt.scatter(ages, salaries)
plt.show()

# salaries5000 = salaries + 1.05
# print(salaries5000)
