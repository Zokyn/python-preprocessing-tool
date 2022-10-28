import numpy as np
import pandas as pd

max_std = 10
data = pd.read_csv('winequality-red.csv', sep=';')

def has_outliners(data, col):   
    if(data[col].std() >= max_std):
        return True;
    else:
        return False;
def column_attributes(data):
    list_of_columns = []
    for col in data.columns:
        attributes = ['mean', 'std', 'max', 'min', 'hasOutliners?']
        column_mean = data[col].mean()
        column_std = data[col].std()
        column_max = data[col].max()
        column_min = data[col].min()
        
        outliners = has_outliners(data, col)

        column = pd.Series([column_mean, column_std, column_max, column_min, outliners], index=[attributes], name=col)

        list_of_columns.append(column)
    return pd.DataFrame(list_of_columns)

print(column_attributes(data));
# print(data)