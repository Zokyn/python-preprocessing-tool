import numpy as np
import pandas as pd

path = 'winequality-red.csv';
s = pd.read_csv(path, sep=';')

print(s)