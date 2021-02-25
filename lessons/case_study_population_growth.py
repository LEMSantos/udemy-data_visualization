# Crescimento da População Brasileira 1980-2016
# DataSus

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/populacao_brasileira.csv', sep=';')

x = df.ano
y = df.population

plt.bar(x, y, color='#ccc')
plt.plot(x, y, color='k', linestyle='--')

plt.title('Crescimento da População Brasileira 1980-2016')
plt.xlabel('Ano')
plt.ylabel('População x 100.000.000')

# plt.show()
plt.savefig('../figures/populacao_brasileira.png', dpi=300)
