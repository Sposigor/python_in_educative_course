import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\IgorD\Desktop\python_educative\python_educative\Predictive Data Analysis with Python\Data Wrangling\housing.csv')

# clean data and drop missing values, usign method IQR
def clean_data(df):

    df = df.dropna() # Remove os valores nulos

    # Lista com as colunas que precisam ser tratadas
    out_list = ['median_house_value', 'median_income', 'housing_median_age']

    quantiles_df = (df.quantile([0.25,0.75])) # Primeiro e ultimo quartil

    for out in out_list: # aplicar o IQR para cada coluna

        Q1 = quantiles_df[out][0.25] # Recuperando o valor do primeiro quartil
        Q3 = quantiles_df[out][0.75] # Recuperando o valor do ultimo quartil

        iqr = Q3 - Q1 # Processando o IQR

        valor_inferior = (Q1 - (iqr * 1.5)) # valor inferior do IQR
        valor_superior = (Q3 + (iqr * 1.5)) # valor superior do IQR

        col = df[out] # Armazena os valores

        col[(col < valor_inferior)] = valor_inferior # Atribuir os valores inferiores sem os outliers

        col[(col > valor_superior)] = valor_superior # Atribui os valores superiores sem os outliers

    return df
