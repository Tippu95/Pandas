import pandas as pd

df = pd.read_csv('./employees.csv')
df2 = pd.read_json('./sample_employees_with_nulls.json')

# getting the dataframe information
print("####### dataframe info ##########")
print(df.info())

# description of the created dataframe
print("####### dataframe description ##########")
print(df.describe())

# head provides 5 sample records from dataframe
print("####### head content ##########")
print(df.head())

# selecting columns data from dataframe
print("####### selected coluymn data ##########")
print(df[['EmployeeID', 'FirstName', 'Department']])
