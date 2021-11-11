import pandas as pd
import numpy as np

# Lendo um arquivo csv
df = pd.read_csv(r'C:\Users\IgorD\Desktop\python_educative\python_educative\Predictive Data Analysis with Python\pandas\test.csv', sep=",")
print(df)

# Criando um csv
df = pd.DataFrame(np.arange(25).reshape(5,5), columns = ['A','B','C','D','E'])
df.to_csv(r'C:\Users\IgorD\Desktop\python_educative\python_educative\Predictive Data Analysis with Python\Data Wrangling\novo.csv')

# Processo de merge de um DataFrame
df1 = pd.DataFrame({'Apontar':['A', 'B', 'C', 'B', 'A', 'D'], 
                    'valores_df1':[0,1,2,3,4,5]})
print("Primeiro DataFrame")
print(df1)

df2 = pd.DataFrame({'Apontar':['B', 'C', 'B','D'], 
                    'valores_df2':[6,7,8,9]})
print("\nSegundo DataFrame")
print(df2)

print("\nMerge do DataFrame")
print('\n',pd.merge(df1, df2)) # Merge de dois DataFrames


# Merge de dois DataFrames a partir da esquerda
df1 = pd.DataFrame({'Apontar':['A', 'B', 'C', 'B', 'A', 'D'], 
                    'valores_df1':[0,1,2,3,4,5]})

df2 = pd.DataFrame({'Apontar':['B', 'C', 'B', 'D', 'E'], 
                    'valores_df2':[6, 7, 8, 9, 12]})

print("Merge a partir da esquerda\n")
print(pd.merge(df1, df2, how = 'left')) # merge a partir da esquerda

# Merge de dois DataFrames a partir da direita
df1 = pd.DataFrame({'Apontar':['A', 'B', 'C', 'B', 'A', 'D'],
                    'valores_df1':[0,1,2,3,4,5]})
df2 = pd.DataFrame({'Apontar':['B', 'C', 'B', 'D', 'E'],
                    'valores_df2':[6, 7, 8, 9, 12]})

print("Merge a partir da direita\n")
print(pd.merge(df1, df2, how = 'right')) # merge a partir da direita

# Merge de dois DataFrames a partir do centro
df1 = pd.DataFrame({'coluna1':['EUA', 'China', 'India', 'Russia', 'Argentina'],
                    'coluna2': ['A', 'B', 'C', 'D', 'H'],
                    'valores_df1': [0,1,2,3,4]})
df2 = pd.DataFrame({'coluna1':['China', 'India', 'Russia', 'Argentina', 'Brazil'],
                    'coluna2': ['A', 'B', 'C', 'D', 'Z'],
                    'valores_df2': [6, 7, 8, 9, 10]})

print("Merge a partir do centro\n")
print(pd.merge(df1, df2, on = ['coluna1', 'coluna2'], how = 'outer')) # merge a partir do centro

# Merge de dois DataFrames a partir do indice
df1 = pd.DataFrame({'Apontar':['A', 'B', 'C', 'B', 'A', 'D'], 
                    'valores_df1':[0,1,2,3,4,5]})

df2 = pd.DataFrame(np.arange(10,13,1), index = ['A', 'B','C'], columns = ['valores'])
print(df2)
print("Merged pelo index\n")
print(pd.merge(df1, df2, left_on='Apontar', right_index=True))

