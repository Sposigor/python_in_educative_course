import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Gerando histogramas

# Histograma 1
dados = np.random.randn(50) # Gerando dados aleatórios
plt.hist(dados, edgecolor='black', bins=20, color='blue') # Gerando histograma

# Histograma 2
dados1 = np.random.randn(50) # Gerando dados aleatórios
dados2 = np.random.randn(50) # Gerando dados aleatórios
# plotando os dados
plt.hist(dados1, density=True, bins=20, color='red', alpha=0.5)
plt.hist(dados2, density=True, bins=20, alpha=0.5)

# Usando seaborn
# dados
set1 = np.random.randn(500)
set2 = np.random.randn(500)
# Plotando os dados
sns1 = sns.jointplot(x=set1, y=set2)
sns2 = sns.jointplot(x=set1, y=set2, kind='hex')

# Plotando todos os graficos
plt.show()

# Mais sobre jointplot https://seaborn.pydata.org/generated/seaborn.jointplot.html
# Mais sobre histogramas https://seaborn.pydata.org/generated/seaborn.distplot.html e https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

