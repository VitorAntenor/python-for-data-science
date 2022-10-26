import numpy as np
import pandas as pd

# labels = ['a','b', 'c'] #lista chamada labels
# minha_lista = [10, 20, 30]
# arr = np.array([10, 20, 30]) #converter lista pra array
# d = {'a':10, 'b':20, 'c':30}

# series = pd.Series(data = minha_lista, index = labels) #data = dado a ser passado, index = forma que vamos acessar os dados dentro do dataframe
# print("********SERIES********")
# print(series)
# print("******************************")

# #buscando valor na series
# print("Buscando valor na series:", series['b'])
# print("******************************")

# #invertendo a series
# series1 = pd.Series(index = minha_lista, data = labels)
# print("Invertendo:")
# print(series1)
# print("******************************")

# #exemplo de series
# ser1 = pd.Series(data = [1,2,3,4], index= ['Brasil', 'EUA', 'Russia', 'Argentina'])
# print("EXEMPLO DE SERIES")
# print(ser1)
# print("******************************")

# #Soma de series
# ser2 = pd.Series(data = [1,2,3,4], index = ['Argentina', 'EUA', 'Brasil', 'Russia'])
# print("SÉRIES 2")
# print(ser2)
# print("******************************")
# print("Soma dos índices:")
# print(ser1 + ser2) #Soma os indices de Brasil com Brasil, Arg com Arg
# print("******************************")

# #DATAFRAME, CRIAÇÃO E FATIAMENTO
# np.random.seed(101) #random = gera valores aleatorios, seed = permite que os mesmos numeros aleatorios sejam vistos em qualquer pc 
# df = pd.DataFrame(data = np.random.randn(5,4), index = 'A B C D E'.split(), columns = ' W X Y Z'.split()) #randn = serie aleatoria, split = forma de fazer uma lista a partir de uma cadeia de strings
# print("DATAFRAME")
# print(df)
# print("******************************")

# #Extraindo dados do dataframe
# ext = df['W']
# print("COLUNA EXTRAÍDA:")
# print(ext)
# print("******************************")

# #Adicionando coluna nova
# df ['new'] = df['W'] + df['X']
# print("NOVO DATAFRAME")
# print(df)
# print("******************************")

# #Deletando a coluna
# df.drop('new', axis =1, inplace= True) #axis = eixo de referencia pra deletar, inplace = pra alterar direto no dataframe e as alterações ficarem salvas
# print("DATAFRAME COM COLUNA DELETADA")
# print(df)
# print("******************************")

# #ENCONTRAR VALORES ESPECIFICOS DENTRO DO DATAFRAME
# print("Encontrando valores especificos no dataframe:", df.loc['A', 'W']) #sempre linha e depois coluna
# print("******************************")

# #ENCONTRARNDO VALORES DE VÁRIAS LINHAS E COLUNAS
# print("Valores de mais linhas e colunas:")
# print(df.loc[['A', 'B'], ['X', 'Y', 'Z'] ])
# print("******************************")

# #df>0
# print("Valores maiores de zero:")
# print(df>0)
# print("******************************")

# #Aparecendo apenas os valores que são maiores que zero
# bol = df > 0
# print("Valores:")
# print(df[bol])
# print("******************************")

# #Verificando linhas específicas que são maiores que zero
# #Nesse caso, vai aparecer as do w, mas vai excluir a linha que for < 0 (linha c)
# print("Linhas maiores que 0:")
# print(df[df['W'] > 0])
# print("******************************")

# #Aparecendo as linhas que são maiores que 0, mas aplicando em outra coluna
# print("Valores com colunas diferentes:")
# print(df[df['W'] > 0 ] ['Y'])

# print("******************************")
# #Valores da coluna W > 0 e Y > 1
# print("Coluna W maior que 0 e Y maior que 1:")
# print(df[(df['W'] > 0 ) & (df['Y'] > 1)])
# print("******************************")

# #Resetando o index

# print("Resetando o index:")
# print(df.reset_index())
# print("******************************")

# #Se eu quiser que alguma outra coluna seja o index temporariamente
# colu = 'RJ SP BA MG GO'.split()
# df['Estado'] = colu

# print("Dataframe atualizado:")
# print(df)
# print("******************************")

# #Fazendo o "Estado" se tornar um index
# print("Agora Estado sendo um índice:")
# print(df.set_index('Estado'))
# print("******************************")

# #ÍNDICES MULTINÍVEIS

# #NÍVEIS DE ÍNDICE
# outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
# inside = [1,2,3,1,2,3]
# hier_index = list(zip(outside, inside)) #método zip é usado pra pegar outside e inside pra criar uma lista de tuplas, pega 2 listas e associa cada valor de uma lista a da outra
# hier_index = pd.MultiIndex.from_tuples(hier_index)
# print(hier_index)
# print("******************************")

# #EXEMPLO DE ÍNDICE MULTINÍVEL
# df1 = pd.DataFrame(np.random.randn(6,2), index = hier_index, columns = ['A', 'B']) 
# print("índice multinível:")
# print(df1)
# print("******************************")

# #DEFININDO NOMES PROS INDICES
# # df2 = df.index.names = ['Grupo', 'Numero']
# # print("Definindo valores para índices:")
# # print(df2)

# #DADOS AUSENTES

# d = {'A': [1,2, np.nan], 'B': [ 5, np.nan, np.nan], 'C': [1,2,3]} #np.nan = dado faltante
# print("Dataframe do dicionario:")
# dfm = pd.DataFrame(d)
# print(dfm)
# print("******************************")

# #EXCLUINDO LINHAS QUE POSSUEM NAN
# th = dfm.dropna(thresh = 2) # thresh = 2 exclui linhas que possuem 2 NaN nela
# print("DATAFRAME APÓS ALTERAÇÕES")
# print(th)
# print("******************************")

# #SUBSTITUINDO NaN POR OUTRA COISA QUALQUER
# cq = dfm.fillna(value = 'X')
# print("Substituindo NaN por outra coisa:")
# print(cq)
# print("******************************")

# #PREENCHENDO OS NaN com os valores anteriores (com os mesmos valores que já tiverem numero)
# va = dfm.fillna(method = 'ffill')
# print("Preenchendo com valores anteriores:")
# print(va)
# print("******************************")

# #GROUP BY
# datagb = {'Empresa': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
# 'Nome': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
# 'Venda': [200, 120, 340, 124, 243, 350]}

# dfgb = pd.DataFrame(datagb)
# print("Dataframe com o dicionário:")
# print(dfgb)
# print("******************************")

# #Realizando o agrupamento por empresa
# group = dfgb.groupby('Empresa')
# print("Soma de vendas por empresa:")
# print(group.sum())
# print("******************************")

# #MÉDIA DE VENDAS POR EMPRESA
# print("Média de vendas por empresa:")
# print(group.mean())
# print("******************************")

# #USANDO MÉTODO PRA ENCONTRAR INFORMAÇÕES PRÉ APLICADAS
# print("Relatório das informações:")
# print(group.describe()) #describe fornece informações como desvio padrão, média, valor max e min encontrado
# print("******************************")

# #AGRUPANDO POR NOME
# group2 = dfgb.groupby('Nome')
# print("Vendas de amy:")
# print(group2.sum().loc['Amy'])
# print("******************************")

#MÉTODOS DE JUNÇÃO DE DATAFRAMES

# dfu = pd.DataFrame({'A':['A0', 'A1','A2', 'A3'],
# 'B':['B0', 'B1', 'B2', 'B3'],
# 'C':['C0', 'C1', 'C2', 'C3'],
# 'D':['D0', 'D1', 'D2', 'D3']},
# index = [0,1,2,3]
# )

# print("DataFrame 1:")
# print(dfu)
# print("******************************")

# dfd = pd.DataFrame({'A':['A4', 'A5','A6', 'A7'],
# 'B':['B4', 'B5', 'B6', 'B7'],
# 'C':['C4', 'C5', 'C6', 'C7'],
# 'D':['D4', 'D5', 'D6', 'D7']},
# index = [4,5,6,7]
# )

# print("DataFrame 2:")
# print(dfd)
# print("******************************")

# dft = pd.DataFrame({'A':['A8', 'A9','A10', 'A11'],
# 'B':['B8', 'B9', 'B10', 'B11'],
# 'C':['C8', 'C9', 'C10', 'C11'],
# 'D':['D8', 'D9', 'D10', 'D11']},
# index = [8,9,10,11]
# )

# print("DataFrame 3:")
# print(dft)
# print("******************************")

# #concatenando os dataframes

# conc = pd.concat([dfu, dfd, dft])
# print("Dataframes concatenados:")
# print(conc)
# print("******************************")

# #mesclando dataframes

# esquerda = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
# 'A':['a0','a1', 'a2', 'a3'],
# 'B':['b0','b1', 'b2', 'b3']})

# print("Dataframe da esquerda:")
# print(esquerda)
# print("******************************")

# direita = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
# 'C':['c0','c1', 'c2', 'c3'],
# 'D':['d0','d1', 'd2', 'd3']})

# print("Dataframe da direita:")
# print(direita)
# print("******************************")

# #mesclando os dataframes
# mes = pd.merge(esquerda, direita, how='inner', on = 'key') # how = união de tabelas em sql, inner = especifica que quero especificar pela chave
# print("Dataframe mesclado:")
# print(mes)
# print("******************************")

# #Exemplo mais complicado
# esquerda1 = pd.DataFrame({'key1': ['k0', 'k1', 'k2', 'k3'],
# 'key2': ['k0', 'k1', 'k0', 'k1'],
# 'A': ['a0', 'a1', 'a2', 'a3'],
# 'B': ['b0', 'b1', 'b2', 'b3']})

# print("Dataframe esquerda 1:")
# print(esquerda1)
# print("******************************")

# direita1 = pd.DataFrame({'key1': ['k0', 'k1', 'k1', 'k2'],
# 'key2': ['k0', 'k0', 'k0', 'k0'],
# 'C': ['c0', 'c1', 'c2', 'c3'],
# 'D': ['d0', 'd1', 'd2', 'd3']})

# print("Dataframe direita 1:")
# print(direita1)
# print("******************************")

# mescex = pd.merge(esquerda1, direita1, on=['key1', 'key2'])
# print("Exemplo mais complicado mesclado:")
# print(mescex) #vai aparecer os mesmos dados que estiverem mesma ordem de keys ex nos 2 dataframes. ex: k0 e k0 no dataframe 1 e k0 e k0 no dataframe 2
# print("******************************")

# #colocando todos os elementos do dataframe
# mescex = pd.merge(esquerda1, direita1, how = 'outer', on = ['key1', 'key2'] )
# print("Colocando todos os elementos no dataframe:")
# print(mescex)

# #JUNTANDO DATAFRAMES (JOIN)
# esqj = pd.DataFrame({'A': ['a0', 'a1', 'a2'],
# 'B': ['b0', 'b1', 'b2']},
# index = ['k0', 'k1', 'k2'])
# print("******************************")

# print("Dataframe 1 que vai usado no join:")
# print(esqj)
# print("******************************")

# dirj = pd.DataFrame({'C': ['c0', 'c2', 'c3'],
# 'D': ['d0', 'd2', 'd3']},
# index = ['k0', 'k2', 'k3'])

# print("Dataframe 2 que vai usado no join:")
# print(dirj)
# print("******************************")

# junt = esqj.join(dirj)

# print("Dataframe após o join:") #colocando os valores de direita sempre que o indice for = o de esquerda
# print(junt)
# print("******************************")

#OPERAÇÕES

# op = pd.DataFrame({'col1': [1,2,3,4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
# print("OPERAÇÕES COM DATAFRAME")
# print(op)
# print("******************************")

# ##VERIFICANDO VALORES ÚNICOS - QUE NÃO SE REPETEM
# print("Retornando o array com valores únicos")
# opu = op['col2'].unique() #Retornando valores da coluna 2, sem repetição
# print(opu)
# print("******************************")

# #Verificando o tamanho de determinado vetor
# optam = op['col2'].nunique()
# print("Imprimindo tamanho do valor sem repetição:")
# print(optam)
# print("******************************")

# #Imrpimindo valores e quantas vezes eles aparecem
# qva = op['col2'].value_counts() #verificando quantas vezes os n° aparecem na col2
# print("Imprimindo numero de vezes que os n° aparecem:")
# print(qva)
# print("******************************")

# #exemplo de seleção de dados
# sdd = op[(op['col1']>2) & (op['col2'] == 444)]
# print("Selecionando dados da col 1  com indice maior que 2 e col2 == 444:")
# print(sdd)
# print("******************************")

# #SOMA DE COLUNAS
# print("Valor da soma da coluna 1:", op['col1'].sum())
# print("******************************")

# #MULTIPLICANDO O VALOR DA COLUNA 1 POR 2 USANDO FUNÇÃO
# def vezes2(x):
#     return x*2

# v2 = op['col1'].apply(vezes2) #APPLY = aplica a função nos parâmetros passados anteriormente
# print("Coluna 1 multiplicando por 2:")
# print(v2)
# print("******************************")

# # #Deletar colunas
# # print("Apagando coluna 2:")
# # del op['col2']
# # print(op)

# #Colocando valores da coluna 2 em ordem crescente
# ordcre = op.sort_values(by= 'col2')
# print("Valores da coluna 2 em ordem crescente:")
# print(ordcre)
# print("******************************")

# #verificando valores nulos
# vnulo = op.isnull()
# print("Valores nulos:")
# print(vnulo)

#ENTRADA E SAÍDA DE DADOS

esd = pd.read_csv('exemplo.csv', sep = ',') #read_csv = especifica o tipo de arquivo que vou manipular (CSV) e o sep = separador dos dados.
print("Dados importados do arquivo exemplo.csv:")
print(esd)
print("******************************")

#somando +1 a todos os dados 
esd2 = esd + 1
print("Somando +1 a todos os dados:")
print(esd2)
print("******************************")

#exportando arquivo .csv
exportar = esd2.to_csv('exemplo2.csv', sep = ',')

#Lendo parte específica de arquivo .xlsx

lendo = pd.read_excel('Exemplo_Excel.xlsx', sheet_name= 'Sheet1') #Sheetname= qual aba quero ler
print("Lendo valores do arquivo importado:")
print(lendo)
print("******************************")

#exportando arquivo .xlsx 
exportando = lendo.to_excel('Exemplo_Excel2.xlsx', sheet_name='Sheet1')

#COMEÇAR AULA 36

