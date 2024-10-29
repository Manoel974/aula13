import pandas as pd 
import numpy as np

df = pd.read_excel('vendas_roupas1.xlsx')
print(df)

categoria = df['Categoria']
quantidade_vendida = df['Quantidade Vendida']
# print(quantidade_vendida.describe()) 
print(quantidade_vendida)
print(categoria)

print(30*'==')

q1 = np.quantile(quantidade_vendida, 0.25)
q2 = np.quantile(quantidade_vendida, 0.50)
q3 = np.quantile(quantidade_vendida, 0.75)

print(f'1° Quartil (Q1): {q1}')
print(f'2° Quartil (Q2): {q2}')
print(f'3° Quartil (Q3): {q3}')

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)

print(30*'==')

print(f'Média: {media}')
print(f'Mediana: {mediana}')

quantidadevdd_organizada = df.sort_values(by='Quantidade Vendida', ascending=True)
quantidade_vendida = quantidadevdd_organizada['Quantidade Vendida']
print(quantidade_vendida.values)