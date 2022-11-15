import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())

# #QUESTÃO 1
# sns.set_style('darkgrid')
# joint = sns.jointplot(x= 'fare', y= 'age', data = titanic)
# plt.show()

#QUESTÃO 2
# sns.set_style('darkgrid')
# displot = sns.displot(titanic['fare'])
# plt.show()

#QUESTÃO 3
# box = sns.boxplot(x = 'class', y = 'age', data = titanic)
# plt.show()

#QUESTÃO 4
# grafico = sns.swarmplot (x = 'class', y = 'age', data = titanic)
# plt.show()

#QUESTÃO 5
# grafcol = sns.countplot(x = 'sex', data = titanic)
# plt.show()

#QUESTÃO 6
# corr = titanic.corr()
# print("Correlação entre as colunas: ")
# print(corr)
# #verificando a correlação em mapas de calor
# heatmap = sns.heatmap(corr, annot = False)
# plt.show()

