import pandas as pd
import numpy as np

# Lendo um arquivo csv
df = pd.read_csv(r'C:\Users\IgorD\Desktop\python_educative\python_educative\Predictive Data Analysis with Python\pandas\test.csv', sep=",")
print(df)

# Criando um csv
df = pd.DataFrame(np.arange(25).reshape(5,5), columns = ['A','B','C','D','E'])
df.to_csv(r'C:\Users\IgorD\Desktop\python_educative\python_educative\Predictive Data Analysis with Python\Data Wrangling\novo.csv')

