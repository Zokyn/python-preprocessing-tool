import numpy as np
import pandas as pd

max_std = 10
data = pd.read_csv('winequality-red.csv', sep=';') # dataset
columns = data.columns; # print(columns) # colunas do dataset

def has_outliners(data, col):   
    if(data[col].std() >= max_std):
        return True;
    else:
        return False;
def column_attributes(data):
    list_of_columns = []
    # Percorre cada coluna do dataset e define seus atributos
    for col in data.columns:
        # Atributos baseado em propriedades estatísticas de cada coluna
        attributes = ['mean', 'std', 'max', 'min', 'hasOutliners?']
        column_mean = data[col].mean()  # MEDIA
        column_std = data[col].std()    # DESVIO PADRÃO    
        column_max = data[col].max()    # VALOR MAXIMO
        column_min = data[col].min()    # VALOR MINIMO 
        # Por ultimo utiliza de uma função para verificar se há outliners
        outliners = has_outliners(data, col)

        column = pd.Series(
            data=[column_mean, column_std, column_max, column_min, outliners], 
            index=[attributes], 
            name=col
        )

        list_of_columns.append(column)
    return pd.DataFrame(list_of_columns)

print(column_attributes(data))