# import os

# os.system('cls')


# media = (2000 + 2500 + 3000 + 3500 + 4000 + 30000) / 6
# print(media)


import numpy as np 

dados_salario = [2000, 2500, 3000, 3500, 4000, 30000]

media = np.mean(dados_salario)
print('Média: ', media)