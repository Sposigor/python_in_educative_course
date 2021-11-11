import pandas as pd
import numpy as np

# Declaração do problema
# Usa sum_swap para calcular a soma dos valores de swap
# A soma dos valores mínimo e máximo de cada linha é calculada.
# Esses valores são atribuídos à nova coluna row_sum.
# A soma do valor mínimo e máximo de cada coluna é calculada.
# Esses valores são atribuídos à nova linha col_sum.
# Finalmente, os novos valores de linha e coluna são trocados.

df = pd.DataFrame(np.random.randint(1, 100, 25).reshape(5, 5))

def Sum_Swap(df):
    # Calcula a soma dos valores da linha
    minm_r = np.min(df, axis = 1)
    maxm_r = np.max(df, axis = 1)
    df['row_sum'] = minm_r + maxm_r
    # Calcula a soma dos valores da coluna
    minm_c = np.min(df, axis = 0)
    maxm_c = np.max(df, axis = 0)
    df.loc['col_sum'] = minm_c + maxm_c
    # armazena os valores da linha e coluna
    a, b = df['row_sum'].copy(), df.loc['col_sum'].copy()
    # Troca os valores da linha e coluna
    df['row_sum'], df.loc['col_sum'] = b, a
    
    return df

df_res = Sum_Swap(df.copy())

print(df_res)