import numpy as np
import pandas as pd

data = pd.read_csv('winequality-red.csv', sep=';')

def verify_std_column():
    for col in data.columns: 
        outliners = False
        std = data[col].std()
        if(std >= 1.0):
            outliners = True

        print(f'{col}: {std} : {outliners}')

def att_column():
    list_of_columns = []
    for col in data.columns:
        attributes = ['mean', 'std', 'max', 'min']
        column_mean = data[col].mean()
        column_std = data[col].std()
        column_max = data[col].max()
        column_min = data[col].min()
        
        column = pd.Series([column_mean, column_std, column_max, column_min], index=[attributes], name=col)

        list_of_columns.append(column)
        # print(column)
        # print(f"'{col}': {column_mean} | {column_std} | {column_max} | {column_min}")
    print(pd.DataFrame(list_of_columns))

att_column();
# print(data)