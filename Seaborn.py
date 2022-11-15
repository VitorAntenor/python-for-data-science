import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#PLOTS CATEGORICOS
tips = sns.load_dataset('tips') #importa o data set do tips (Dados categoricos possuem textos e poucas possibilidades de consulta)

print(tips.head()) 
print("*****************************")

#DISPLOT = pega os dados e faz uma distribuição, depois faz uma curva kde
# dispolt = sns.displot(tips['total_bill'], kde = False)
# plt.show()

#Joint plot = verifica qual a distribuição conjunta do total bill com o tip (conta com a gorjeta dada)
# joint = sns.jointplot(x = 'total_bill', y = 'tip', data = tips) #existe uma relação linear entre eles, quanto maior a conta, maior a gorjeta
# plt.show()

#Barplot
# grafico = sns.barplot(x = 'sex', y= 'total_bill', data = tips)
# print("Exibindo gráfico: ")
# plt.show()
# print("*****************************")

#COUNT PLOT (Conta os elementos em um eixo, não tem o eixo y pois nele já vai ter as contagens)
# grafic = sns.countplot(x = 'sex', data = tips)
# plt.show()

#BOX PLOT
# grafic2 = sns.boxplot(x = 'day', y= 'total_bill', data = tips) #da primeira barra em preto até a segunda é onde tá os primeiros 25% dos dados, da segunda até o meio, 50%, do meio até a próxima 75%, acima disso  é o total
# plt.show()

#VIOLIN PLOT
# violin = sns.violinplot(x = 'day', y = 'tip', data = tips, hue = 'sex', split = True) #o seaborn criou distribuições de probabilidades pro conjunto de dados baseado no modelo não paramétrico. o ponto branco no meio dos dados significa a média. O hue "quebra os dados" para homem e mulher, nesse caso.
# #O split pega a metade de um gráfico e junta com o do outro (metade do masc e metade do fem)
# plt.show()

# STRIP PLOT - Só plota pontos apenas onde os dados aparecem
# stripplot = sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True) #O jitter afasta um pouco os pontos para não ficarem próximos
# plt.show()

#Swarm plot - coloca um dado ao lado do outro (um ponto do lado do outro) conforma eles aparecem
# swarmplot = sns.swarmplot(x = 'day', y = 'total_bill', data = tips)
# plt.show()

# PLOTS MATRICIAIS
# flights = sns.load_dataset('flights')
# print(flights.head())
# print("*****************************")

# #verificando a correlação entre as colunas
# corr = flights.corr()
# print("Correlação entre todas as variáveis (dados categóricos não entram)")
# print(corr)

# #verificando a correlação em mapas de calor
# mapacalor = sns.heatmap(corr, annot = True) #Annot mostra os valores dentro do quadrado
# plt.show()

#Reorganizando os dados para mostrar passageiros por todos os meses durante alguns anos
# pivo = flights.pivot_table(values ='passengers', index = 'month', columns = 'year')
# print(pivo)

#plotando o mapa de calor
# print(sns.heatmap(pivo, linewidths = 1)) #linewidths facilita a visualização, colocando os anos como quadrados
# plt.show() #é possivel perceber que nos meses de jul e aug o numero de voos é maior (verão dos eua)

#CLUSTER MAP - PEGA OS DADOS E CRIA CLUSTERS, AGRUPANDO EM CONJUNTOS
# print(sns.clustermap(pivo))
# plt.show()

#PLOTS DE REGRESSÃO

#Fazendo uma regressão linear entre o total da conta e o tip
# print(sns.lmplot(x= 'total_bill', y='tip', data = tips, hue ='sex', markers=['o', 'v'])) #markers separa entre bolinha e triangulo
# plt.show()

#PairGrids - permite a construção de gráficos com maiores detalhes
# iris = sns.load_dataset('iris')
# print(iris.head(20))

# g= sns.PairGrid(iris)
# print(g)
# plt.show()

# cor = sns.countplot(x= 'sex', data = tips)
# plt.show()

#mudando cor de fundo do gráfico
sns.set_style('darkgrid') #linha responsável por mudar a cor do fundo dos graficos
plt.figure(figsize=(6,4)) #reponsável por alterar o tamanho da figura
cordark = sns.countplot(x='sex', data = tips)
plt.show()