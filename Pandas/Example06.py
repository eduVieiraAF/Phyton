import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))  # 10 first row of the data
print(df.head())  # by default, it is the first 5
print(df.tail()) # last rows

df2 = pd.read_json('data.json')
print(df2.info())
