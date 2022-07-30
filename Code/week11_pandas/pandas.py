import pandas as pd

listData = [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33]
]

df = pd.DataFrame(listData, columns=['name', 'subject', 'grade'])
print(df)
