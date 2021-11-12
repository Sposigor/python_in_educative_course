import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os dados
set1 = np.random.randn(220) 
# Plotando os dados
sns1 = sns.boxplot(set1, color='red', whis=np.inf)
plt.show()