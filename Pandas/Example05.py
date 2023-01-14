import pandas as pd

df = pd.read_json('data.json')
print(df)
print(df.to_string())
