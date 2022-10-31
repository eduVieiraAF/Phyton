#? Data frame
#* It's a 2 dimensional data structure

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

data_frame = pd.DataFrame(data)
print(data_frame)

# Locating row
print(data_frame.loc[0])

# returning row 0 and 1
print(data_frame.loc[[0,1]])

# named indexes
indexed_data = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(indexed_data)

# locating named indexes
print(indexed_data.loc["day3"])

