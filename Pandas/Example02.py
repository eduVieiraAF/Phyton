import pandas as pd

my_dataset = ["JS", "TS", "Python", "Kotlin"]
my_data = pd.Series(my_dataset)
print(my_data)
print(my_data[1])

my_data2 = pd.Series(my_dataset, index= ["a", "b", "c", "d"]) # labels
print(my_data2)
print(my_data2[2])

my_dataset3 = {"day1": 420, "day2": 380, "day3": 390}
my_data3 = pd.Series(my_dataset3)
print(my_data3)