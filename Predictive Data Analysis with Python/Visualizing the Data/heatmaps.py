import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregadno o arquivo
url = 'https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv'
df = pd.read_csv(url)

# Criando o gráfico
df = pd.pivot_table(df, values='lifeExp', index=['continent'], columns='year')

# Plotando o gráfico
sns1 = sns.heatmap(df, annot=True, fmt='.2f')
plt.show()

# Mais sobre heatmaps: https://seaborn.pydata.org/generated/seaborn.heatmap.html