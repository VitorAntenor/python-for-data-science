import numpy as np

print("**********")
print("QUESTÃO 1")
matz = np.zeros(10)
print("Matriz de 10 zeros:", matz)

print("**********")
print("QUESTÃO 2")
mtzu = np.ones(10)
print("Matriz de 10 numeros 1:", mtzu)
print("**********")

print("**********")
print("QUESTÃO 3")
mdc= np.ones(10) * 5
print("Vetor de 10 números 5:", mdc)
print("**********")

print("QUESTÃO 4")
mtzcq = np.arange(10,51)
print("Vetor de 10 a 50:", mtzcq)
print("**********")

print("QUESTÃO 5")
mtzp = np.arange(10,51,2)
print("Vetor dos numeros pares de 10 ate 50:", mtzp)
print("**********")

print("QUESTÃO 6")
mtzt = np.arange(9).reshape(3,3)
print("Vetor de 0 a 8:", mtzt)
print("**********")

print("QUESTÃO 7")
print("Matriz identidade 3x3:")
print(np.eye(3))
print("**********")

print("QUESTÃO 8")
mtzal = np.random.rand(4)
print("Números aleatorios entre 0 e 1:", mtzal)
print("**********")

print("QUESTÃO 9")
vcv= np.random.randn(25)
print("25 vetores:", vcv)
print("**********")

print("QUESTÃO 10")
sm = np.arange(1,101).reshape(10,10) / 100
print("Crie a seguinte matriz:", sm)

print("INDEXAÇÃO NUMPY E SELEÇÃO")
print("**********")

mati = np.arange(1,26).reshape(5,5)
print("MATRIZ MODELO:", mati) 
print("**********")

print("QUESTÃO 1 (Tirar linhas e colunas):", mati[2:,1:]) 
print("**********")

print("QUESTÃO 2:")
print("Aparecendo elemento 20:", mati[3,4])
print("**********")

print("QUESTÃO 3")
print("Escolhendo registros para aparecerem:", mati[:3, 1:2])
print("**********")

print("QUESTÃO 4:", mati[4:][:])
print("**********")
print("QUESTÃO 5:", mati[3:][:])
print("**********")

print("PARTE 3 DOS EXERCÍCIOS")
print("**********")

print("QUESTÃO 1:")
print("Soma dos valores:", mati.sum())
print("**********")

print("QUESTÃO 2:")
print("Desvio padrão:", np.std(mati))
print("**********")










