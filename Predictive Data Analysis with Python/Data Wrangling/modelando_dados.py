import pandas as pd
import numpy as np

# Remodelagem de dados
# Tecnicas mais comuns são Empilhamento, Desempilhamento e Pivotando(dinamica)

# Pilhar dados https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html
df = pd.DataFrame(np.arange(12).reshape(3,4), index = ['Row1', 'Row2', 'Row3'], 
                                            columns = ['Col1','Col2','Col3','Col4',])

df.index.name = 'Row'
df.columns.name = 'Column'

print("DataFrame Original")
print(df,'\n')

print("Dataframe Empilhado")
print(df.stack())

# Desempilhar dados https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html

df = pd.DataFrame(np.arange(12).reshape(3,4), index = ['Row1', 'Row2', 'Row3'], 
                                            columns = ['Col1','Col2','Col3','Col4',])

df.index.name = 'Row'
df.columns.name = 'Column'

print("DataFrame Original")
print(df,'\n')

stacked_df = df.stack()
print("Dataframe Empilhado\n", stacked_df)

print("\nDataFrame desempilhado")
print(stacked_df.unstack(),'\n')

print("DataFrame desempilhado pelo index")
print(stacked_df.unstack('Row'))

# Tabelas Dinamincas https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html

df = pd.DataFrame({'Companhia': ['Google', 'Microsoft', 'Google', 'Microsoft'], 
      'Produto': ['Editor', 'Editor', 'Calendario', 'Azure'], 
      'Preço': ['R$200', 'R$250', 'R$50', 'R$400']})

df.index.name = 'Row'
df.columns.name = 'Column'

print("Dataframe Original")
print(df,'\n')

print("Dataframe Dinamico")
print(df.pivot('Companhia', 'Produto', 'Preço'))

# Mapeamento de dados e localização de duplicados https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html
df = pd.DataFrame({'Cidade':['Lahore', 'Mumbai', 'Karachi', 'Londres'],
                   'AQI':[147, 166, 152, 81]}) # AQI é o indice de qualidade de ar

print("DataFrame Original")
print(df,'\n')

dict_map = {'Lahore':'Pakistão', 'Karachi':'Pakistão', 'Mumbai':'India', 'Londres':'UK'}

df['Pais'] = df['Cidade'].map(dict_map)

print("Mapeamento do DataFrame\n")
print(df)

# Removendo duplicatas
df = pd.DataFrame({'Col1':['A', 'B', 'A', 'C', 'B', 'C'],
                    'Col2': [1, 2, 1, 3, 4, 3]})

print("\nDataFrame Original")
print(df,'\n')

print("\nDataFrame com duplicatas")
print(df.drop_duplicates(),'\n')

print("\nDataFrame sem duplicatas")
print(df.drop_duplicates(['Col1']))

# Substituir e renomear os dados
# Series
srs = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
print('Series original')
print(srs, "\n")

print('Valor unico alterado')
print(srs.replace(1, 'um'), "\n")

print('Varios valores alterados')
print(srs.replace([1, 2, 3], ['um', 'dois', 'tres']), "\n")

# DataFrame

import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\IgorD\Desktop\python_educative\python_educative\Predictive Data Analysis with Python\Data Wrangling\real_estate.csv')

print("Valor unico alterado no DataFrame:")
df = df.replace("SACRAMENTO", "Alterado SACRAMENTO")
print(df.head(), '\n')

print("Valores multiplos alterados no DataFrame:")
df = df.replace(["Alterado SACRAMENTO",'CA'], ["Novo SACRAMENTO","AC"])
print(df.head())


# Renomenado os indices usando rename()

df = pd.DataFrame(abs(np.random.randn(10).reshape(5,2)), index = ['A', 'B', 'C', 'D', 'E'],
                  columns = ['one', 'two'])

print("\nDataframe Original", df)
print("\nTodos os indices alterados", df.rename(index = str.upper, columns = str.title), "\n")

print('\nIndice especifico')
print(df.rename(index={'A':'A index'}, columns={'one':'One'}))

