import pandas as pd
import numpy as np

# Reidexando em series

# Definir a series com valores e indices
srs = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2], index = ['China', 'India', 'EUA', 'Brasil', 'Argentina'])


# Nomeando a series
srs.name = "Taxa de crescimento"

# Nomeando os indices
srs.index.name = "Pais"

srs2 = srs.reindex(['China', 'India', 'Mexico', 'USA', 'Brazil', 'Argentina', 'Espanha'])
print("Nova Series indexada sem tratar NaN:\n",srs2)

srs3 = srs.reindex(['China', 'India', 'Mexico', 'USA', 'Brazil', 'Argentina', 'Espanha'], fill_value=0)
print("\nNova Series indexada com tratamento do NaN:\n",srs3)
