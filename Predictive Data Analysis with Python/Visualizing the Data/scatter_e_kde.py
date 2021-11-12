import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Plotando os dados com scatterplot
# Carregando os dados
df = sns.load_dataset('tips')
# Plotando os dados
sns1 = sns.scatterplot(x = 'total_bill', y = 'tip', data = df)
plt.show()
# Mais sobre scatterplot https://seaborn.pydata.org/generated/seaborn.scatterplot.html


# Plotando os dados com kernel density estimation
x = np.random.randn(1000) # Carregando os dados
sns2 = sns.kdeplot(x, color = 'red') # Plotando o KDE com os dados
plt.show()

# Mais sobre kernel density estimation https://seaborn.pydata.org/generated/seaborn.kdeplot.html e https://en.wikipedia.org/wiki/Kernel_density_estimation
