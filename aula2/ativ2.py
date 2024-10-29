import pandas as pd
import numpy as np

df = pd.read_excel('vendas_eletos_eletronicos2.xlsx')
print(df)
mais_vendidos = df['Total']

valor_total = [18000, 72000, 76000, 94500, 12000, 18000, 7500, 49000, 15000, 14000, 21960, 51981, 19725, 7700, 4250, 3980, 14000, 66000, 26376, 7840]

print(30*'==')

media = np.mean(valor_total)
print('Média: ', media)

mediana = np.median(valor_total)
print('Mediana: ', mediana)

print(30*'==')

q1 = np.quantile(valor_total, 0.25)
q2 = np.quantile(valor_total, 0.50)
q3 = np.quantile(valor_total, 0.75)

print(f'1° Quartil: {q1} 25% das vendas abaixo')
print(f'2° Quartil: {q2} 50% das vendas abaixo')
print(f'3° Quartil: {q3} 70% das vendas abaixo')

print(30*'==')


total_mais_vendidos = df.sort_values(by='Total', ascending=False)
print(total_mais_vendidos)


