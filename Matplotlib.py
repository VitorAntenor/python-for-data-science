import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5, 11)
print("Vetor x:", x)
y = x * x
print("Vetor y:",y)

# # #Plotando o gráfico de 2 variáveis
# # print(plt.plot(x,y))
# # plt.xlabel('Eixo x')
# # plt.ylabel('Eixo y')
# # plt.title('Título')
# # plt.show()
# # print("************************************************************")

# # #Plotando mais de um gráfico
# # plt.subplots(1, 2) #1 = numero de linhas, 2= numero de colunas
# # plt.show()

# #Escolhendo com qual gráfico quero trabalhar
# plt.subplot(1,2,1) #O último numero 1 se refere a qual dos 2 graficos quero trabalhar
# plt.plot(x,y, 'r--')

# plt.subplot(1,2,2) #trabalhando com gráfico 2
# plt.plot(y,x, 'g*-')
# plt.show()

# #SUBPLOTS
# fig, ax = plt.subplots() #cria e figura e os eixos, fica vazio pois não tem nenhum parâmetro
# ax.plot(x, x**3, 'b--') #Plota o x, y = x**3 e cor b-- = azul
# ax.plot(x, x**4, 'g-.')
# ax.set_xlabel('Eixo X')
# ax.set_ylabel('Eixo y')
# ax.set_title('Título do gráfico')
# plt.show()

# #PLOTANDO 2 GRÁFICOS E PREENCHENDO VALORES
# fig, ax = plt.subplots(nrows = 1, ncols = 2)
# ax[0].plot(x,y, 'b')
# ax[0].set_title('Título Gráfico 1')

# ax[1].plot(x,y, 'b')
# ax[1].set_title('Título Gráfico 2')
# plt.show()

# fig, axes = plt.subplots(figsize=(8,4)) #figsize=(8,4) = define largura e altura do gráfico
# axes.plot(x,y, 'r--')
# axes.set_title('Título')
# plt.show()

# #SALVANDO GRÁFICO COMO IMAGEM   
# fig.savefig("imagem.jpg")
# plt.show()

#ADICIONANDO LEGENDA AO GRÁFICO
# fig3, ax3 = plt.subplots() #cria e figura e os eixos, fica vazio pois não tem nenhum parâmetro
# ax3.plot(x, x**3, 'b--', label = 'X ** 3') #Plota o x, y = x**3 e cor b-- = azul
# ax3.plot(x, x**4, 'g-.', label = 'X ** 4')
# ax3.set_xlabel('Eixo X')
# ax3.set_ylabel('Eixo y')
# ax3.set_title('Título do gráfico')
# ax3.legend()
# plt.show()

#PARTE 3
# fig, ax = plt.subplots()
# ax.plot(x, x**2, 'g-', lw = 2) #lw= grossura da linha
# ax.plot(x, x **3, 'b--')
# plt.show()

#DEFININDO OS LIMITES DE X E Y (ATÉ ONDE ELES VÃO NO GRÁFICO)
fig, ax = plt.subplots()
ax.plot(x, x**2, 'g-', lw = 2) #lw= grossura da linha
ax.plot(x, x **3, 'b--')

ax.set_xlim([0,2])
ax.set_ylim([0,10])
plt.show()
