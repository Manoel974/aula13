import numpy as np


valor_casas = [150.000, 180.000, 200.000, 220.000, 250.000, 280.000, 300.000, 320.000, 400.000, 1.500000]


media = np.mean(valor_casas)
print('Média: ', media)

mediana = np.median(valor_casas)
print('Mediana: ', mediana)


print('mediana se mostra o valor mais util para representar dados em cenários com valores extremos')