import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Primeiro desafio, plotar usando o Heatmap. 
df = sns.load_dataset('flights')
df = pd.pivot_table(df, values='passengers', index=['month'], columns='year')
sns1 = sns.heatmap(df, annot=True, fmt='.2f')
plt.show()

# Segundo desafio, plotar usando o lmplot.
df = sns.load_dataset('anscombe')
sns = sns.lmplot(x='x', y='y', data=df, hue='dataset', col='dataset',)
plt.show()
