import numpy as np

minha_lista = [1,2,3]
#array de 1 dimensão (1 dimensões é pq tem 1 colchete)
print("Array de 1 dimensão:")
print(np.array(minha_lista))
print("**********")

#array de 2 dimensões (2 dimensões é pq tem 2 colchetes)
print("Array de 2 dimensões:")
minha_matriz = [[1,2,3], [4,5,6], [7,8,9]]
print(np.array(minha_matriz))
print("**********")

#Arange = cria sequencia de numeros, pede 2 numeros (de inicio e termino)
print("Arange:")
print(np.arange(0,10))
print("**********")

#zeros = cria uma matriz zerada
print("matriz zerada:")
print(np.zeros(3))
print("**********")

#Matriz 5x5 zerada
print("matriz 5x5 zerada")
print(np.zeros((5,5)))
print("**********")

#Matriz com numero 1
print("Matriz com 1:")
print(np.ones(1))
print("**********")

#matriz com 1 na diagonal
print("matriz com 1 na diagonal:")
print(np.eye(4))
print("**********")

#Linspace = especifica inicio, final e intervalo usado pra criar os inteiros
print("Linspace:")
print(np.linspace(0,10, 3))
print("**********")

#Random = cria numeros aleatórios baseados em regras diferentes
#Rand = cria numeros aleatorios de 0 a 1. O 5 é a quant de numeros
print("Random:")
print(np.random.rand(5))
print("**********")

#Gera valores inteiros aleatorios dentro de um intervalo. (0,100,10) 0 a 100 = intervalo
print("Rand int:")
print(np.random.randint(0,100,10))
print("**********")

#Método max encontra o maior valor do vetor
print("MAX:")
art = np.random.rand(20)
print(art)
print("Maior valor dentro do vetor:", art.max())
print("Menor valor dentro do vetor:", art.min())
print("Maior valor por posição:", art.argmax())
print("Menor valor por posição:", art.argmin())
print("**********")

#Reshape = define o tamanho do vetor (linhas x colunas)
valores = np.arange(50).reshape((5,10))
print("Vetor 5x10:", valores)
#Shape = mostra o tamanho do vetor
print("Tamanho do vetor:", valores.shape)
print("**********")

#Definindo quais linhas e colunas quero que apareça
#[:3] = linhas
#[:] = colunas
print("Aparecendo 3 linhas completas:", valores[:3][:])
#criando um novo vetor que h=eh igual as 2 primeiras linhas do "valores"
valores2 = valores[:2].copy()
print("Vetor de teste:", valores2)
print("**********")

#Testando verdadeiro ou falso pros vetores
# vof = np.arange(50).reshape(5,10)
vof = np.random.randint(0,100,10)
print("Vetor de teste:", vof)
print("Vetor de verdadeiro ou falso:", vof < 30)
print("**********")

#Operações com arrays
print("Operações com vetores")
op1 = np.random.randint(0, 15, 20)
print("Array 1:", op1)

op2 = np.random.randint(15,30, 20)
print("Array 2:", op2)

print("Soma dos vetores:", op1 + op2) #Os vetores precisam ter o mesmo tamanho
print("Subtração de vetores:", op2 - op1)
print("Multiplicação de vetores:", op1 * op2)
# print("Divisão de vetores:", op2 / op1)
#Somando vetores a escalares (numeros qualquer)
print("Soma vetor 1 com escalar:", op1 + 100)
print("**********")

print("Calculando raiz quadrada dos vetores")
print("Raiz quadrada vetor 1:", np.sqrt(op1))

#Média do array
print("Média do array:", np.mean(op1))
print("Desvio padrão do vetor 1:", np.std(op1))





