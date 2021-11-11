# Agrupamento de dados
import pandas as pd
import numpy as np

# Vamos usar o groupby para agrupar os dados

df = pd.DataFrame({'p1':['A','A','B','B','C','C'],'p2':['G1','G2','G1','G2','G1','G2'],
    'val_1':np.random.randn(6),'val_2':np.random.randn(6)})
print(df, '\n')
print("DataFrame após usar o GroupBy", '\n')
print(df.groupby(['p1','p2']).mean(), '\n')
print("Ou", '\n')
print(df.groupby('p1').max(), '\n')

# Agregação de dados

df = pd.DataFrame({'Tipo_Animal':[np.random.choice(['Cachorro','Gato','Galinha','Baleia','Cobra','Porco']) for i in range(1, 16)],
                   'Pernas':[np.random.choice(range(1, 4)) for i in range(1, 16)],
                   'Peso':[np.random.choice(range(10, 20)) for i in range(1, 16)],
                   'Altura':[np.random.choice(range(1, 20)) for i in range(1, 16)],
                   'Proteina':abs(np.random.randn(15))})

print("DataFrame Original:")
print(df, '\n')

group = df.groupby('Tipo_Animal') # Agrupamento por tipo de animal

print("Agregar os dados pelo aggregate:")
print(group.aggregate(np.mean), '\n')

