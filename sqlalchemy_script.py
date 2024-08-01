from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import random

DATABASE_URL = 'mysql+pymysql://root:Nagesh%409665@localhost:3306/rnt_crud'

engine = create_engine(DATABASE_URL)

print("----------------------------------------------------------------------------------------------------------")

print("Task-1: Print all data")
print("----------------------------------------------------------------------------------------------------------")

df = pd.read_sql_table("students", engine)
print()
print(df)
print()
print()

print("----------------------------------------------------------------------------------------------------------")

print("Task-2: Print data only roll number greater then 25")
print("----------------------------------------------------------------------------------------------------------")
print()
filtered_data = df[df['roll_no'] > 25]
print(filtered_data)
print()
print()

print("----------------------------------------------------------------------------------------------------------")
print('Task-3: replace values withing dataframe and print')
print("----------------------------------------------------------------------------------------------------------")
print()
for i in filtered_data.index:
        if filtered_data.loc[i, 'name'] == "Samarth":
            filtered_data.loc[i, 'name'] = "Kalburgi"

# filtered_data['name'] = filtered_data['name'].replace("Samarth", "Kalburgi")

print("Modofied Data")
print()
print(filtered_data)
print()

print("----------------------------------------------------------------------------------------------------------")
print("Task-4 : append 2 dataframe (dummy df with random data but with same columns counts)")
print("----------------------------------------------------------------------------------------------------------")

dummy_data = {
        'roll_no': np.random.randint(100, 200, size=2),
        'name': ['Manadev', 'Vishnu'],
        
        'phone': [str(random.randint(1000000000, 9999999999)) for _ in range(2)]
    }

dummy_df = pd.DataFrame(dummy_data)

combined_df = pd.concat([filtered_data, dummy_df], ignore_index=True)

print()
print("Combined DataFrame:")
print()
print(combined_df)

#----------------------------------------------------------------------------------------------------------