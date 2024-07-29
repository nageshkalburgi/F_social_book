import pandas as pd

# Create a list of dictionaries with 10 rows and 3 columns
data = [
    {'Column1': i, 'Column2': i*2, 'Column3': i*3}
    for i in range(10)
]

# Create a DataFrame
df = pd.DataFrame(data)

print("DataFrame Created:")
print(df)

filtered_df = df[df['Column2'] > 5]
print("Filtered DataFrame (Column2 > 5):")
print(filtered_df)

filtered_df_2 = df[(df['Column1'] < 5) & (df['Column3'] > 10)]
print("Filtered DataFrame (Column1 < 5 and Column3 > 10):")
print(filtered_df_2)

df.loc[df['Column1'] == 2, 'Column2'] = -1
print("DataFrame with Replaced Values:")
print(df)

import numpy as np

# Create another DataFrame with the same columns
data2 = [
    {'Column1': i + 10, 'Column2': (i + 10) * 2, 'Column3': (i + 10) * 3}
    for i in range(10)
]

df2 = pd.DataFrame(data2)

# Append df2 to df
appended_df = pd.concat([df, df2], ignore_index=True)
print("Appended DataFrame:")
print(appended_df)
