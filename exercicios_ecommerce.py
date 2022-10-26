import numpy as np
import pandas as pd

#QUESTÃO 1
ecom = pd.read_csv("Ecommerce Purchases")
print("DataFrame de Ecommerce:")
print(ecom)
print("************************************************************")

#QUESTÃO 2
print("Verificando head do dataframe:")
verhead = ecom.head()
print(verhead)
print("************************************************************")

#QUESTÃO 3
print("Tamanho do dataframe:")
tamanho = ecom.info()
print(tamanho)
print("************************************************************")

#QUESTÃO 4
print("Valor médio de compras:")
medio_compras = ecom['Purchase Price'].mean()
print(medio_compras)
print("************************************************************")

#QUESTÃO 5
mais_alto = ecom['Purchase Price'].max()
print("Maior preço de compra:", mais_alto)
mais_baixo = ecom['Purchase Price'].min()
print("Preço de compra mais baixo:", mais_baixo)
print("************************************************************")

#QUESTÃO 6
usam_en = ecom[ecom['Language'] == 'en'].count()
print("Pessoas que usam inglês:")
print(usam_en)
print("************************************************************")

#QUESTÃO 7
advog = ecom[ecom['Job'] == 'Lawyer'].shape
print("Pessoas que tem o cargo de advogado")
print(advog)
print("************************************************************")

#QUESTÃO 8
am = ecom['AM or PM'].value_counts()
print("Pessoas que compraram durante a manhã:")
print(am)
print("************************************************************")

#QUESTÃO 9
mcomuns = ecom['Job'].value_counts()
print("Trabalhos mais comuns")
print(mcomuns)
print("************************************************************")

#QUESTÃO 10
compralot = ecom[ecom['Lot']=='90 WT']
print("Preço da compra")
print(compralot)
print("************************************************************")

#QUESTÃO 11
numerocartao = ecom[ecom['Credit Card']== 4926535242672853]['Email']
print("Email da pessoa com cartão do numero citado:")
print(numerocartao)
print("************************************************************")

#QUESTÃO 12
fornecedor = ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']> 95)]
print("Pessoas com o fornecedor citado:")
print(fornecedor)