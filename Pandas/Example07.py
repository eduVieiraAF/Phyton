import pandas as pd

df = pd.read_csv('data.csv')
df2 = df.dropna()  # gets rids of empty cells

print(df2.to_string())

df3 = pd.read_csv('data.csv')
df3.dropna(inplace=True)
print(df.to_string())

df4 = pd.read_csv('data.csv')
df4.fillna(130, inplace=True)
print(df4.to_string())

#Replacing using mean, median, or mode
x = df["Calories"].mean()
# x = df["Calories"].median()
# x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)
print(df.to_string())
