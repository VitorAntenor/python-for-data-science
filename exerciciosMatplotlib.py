import matplotlib.pyplot as plt
import numpy as np

#QUESTÃO 1
x= np.linspace(0,5, 11)
y= x + 1

# fig, ax = plt.subplots()
# ax.plot(x, x+1, 'b-')
# ax.set_xlabel('Eixo X')
# ax.set_ylabel('Eixo Y')
# ax.set_title('Título do gráfico')

# plt.show()

# #QUESTÃO 2
# fig1 = plt.figure()
# ax1 = fig1.add_axes([0,0,1,1])
# ax2 = fig1.add_axes([0.2, 0.5, 0.2, 0.2])

# plt.show()

#QUESTÃO 3

# fig1= plt.figure()
# ax1= fig1.add_axes([0,0,1,1])
# ax2 = fig1.add_axes([0.2, 0.5, 0.2, 0.2])

# ax1.plot(x, y)
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')

# ax2.plot(x,y)
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')

# plt.show()

#QUESTÃO 4
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])

plt.show()

#ABRIR NOVO DOC E COMEÇAR AULA 47