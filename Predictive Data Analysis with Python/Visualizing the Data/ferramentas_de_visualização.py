# Algumas bibliotecas para visualização de dados
# Vamos usar o matplotlib e o seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Matplotlib
# Gerando uma serie temporal
ponto = np.arange(0, 10, 0.1)

# Plotando o ponto
plt.plot(ponto, np.sin(ponto))

# Titulo do plot
plt.title("Onda")

# Nome dos eixo x
plt.xlabel(xlabel="Tempo")

# Nome dos eixo y
plt.ylabel(ylabel="Amplitude")


# Seaborn
# Gerando dados bivariados correlacionados
r = np.random.RandomState(5)
media = [0, 0]
cov = [(5, 1), (1, 5)]
var1, var2 = r.multivariate_normal(media, cov, 500).T
var1 = pd.Series(var1, name='X-axis')
var2 = pd.Series(var2, name='Y-axis')

# Plotando os dados
sns1 = sns.jointplot(x=var1, y=var2, kind='scatter')

# Gerando ambos os plots
plt.show()