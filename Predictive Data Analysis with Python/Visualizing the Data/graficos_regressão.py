import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Graficos de regressão
# Vamos usar o implot https://seaborn.pydata.org/generated/seaborn.lmplot.html
# Carregamos o dataset e plotamos o gráfico
df = sns.load_dataset('tips')

sns = sns.lmplot(data=df, x='total_bill', y='tip', hue='sex')

plt.show()
