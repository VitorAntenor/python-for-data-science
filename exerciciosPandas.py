import numpy as np
import pandas as pd

#QUESTÃO 1
sal = pd.read_csv('Salaries.csv', sep =',')
print("Importando arquivo .csv:")
print(sal)
print("************************************************************")

#QUESTÃO 2
ver = sal.head()
print("Verificando head:")
print(ver)
print("************************************************************")

#QUESTÃO 3
print("Info:")
informa = sal.info()
print(informa)
print("************************************************************")

#QUESTÃO 4
#Basepay médio

media = sal['BasePay'].mean()
print("BasePay médio:")
print(media)
print("************************************************************")

#QUESTÃO 5
print("Maior quantidade de OvertimePay:")
maior = sal['OvertimePay'].max()
print(maior)
print("************************************************************")

#QUESTÃO 6
cargo = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
print("Cargo de JOSEPH DRISCOLL:")
print(cargo)
print("************************************************************")

#QUESTÃO 7
ganha = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
print("Salário de JOSEPH DRISCOLL:")
print(ganha)
print("************************************************************")

#QUESTÃO 8
print("Pessoa mais bem paga")
mbp = sal['TotalPayBenefits'].max()
print(mbp)
print("\n")
npes = sal[sal['TotalPayBenefits'] == 567595.43]['EmployeeName']
print("O salário é referente a:")
print(npes)
print("************************************************************")

#QUESTÃO 9
print("Pessoa menos bem paga")
menos = sal['TotalPayBenefits'].min()
print("O menor salario é:", menos)
print("\n")
menor = sal[sal['TotalPayBenefits'] == -618.13]['EmployeeName']
print("O salário é referente a:")
print(menor)
print("************************************************************")

#QUESTÃO 10
porano = sal.groupby('Year').mean()['BasePay']
print("Média basepay por ano:")
print(porano)
print("************************************************************")

#QUESTÃO 11
titulostrab = sal['JobTitle'].unique()
print("Trabalhos que não se repetem:")
print(titulostrab)
print("************************************************************")

#QUESTÃO 12
cincoprincipais = sal['JobTitle'].value_counts().head()
print("Principais empregos mais comuns:")
print(cincoprincipais)

