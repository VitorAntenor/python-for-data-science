

print("*****QUESTAO 1 *****")
exp = 7
result = 7 ** 4
print("O resultado da exponenciacao eh:", result)

print("*****QUESTAO 2 *****")
s = 'Ola, pai!'
print(s.split())

print("*****QUESTAO 3 *****")
text = "O diametro da {planeta} eh de {diametro} quilometros.".format(planeta='Terra', diametro= '12742')
print(text)

print("*****QUESTAO 4 *****")
lst = [1,2,[3,4],[5,[100,200,['olá']],23,11],1,7]

dic = {'Valor1' : 1, 'Valor2' : 2, 'Valor3' : [3,4], 'Valor4' : 5, 'Valor5' : 100,
'Valor6' : 200, 'Valor7' : 'olá', 'Valor8' : 23,}

print("Impressão:", dic['Valor7'])

print("*****QUESTAO 5 *****")
d = {'k1':[1,2,3,{'café':['banana','mulher','colher',{'alvo':[1,2,3,'olá']}]}]}

dicio = {'Valor1' : 'k1', 'Valor2' : 1, 'Valor3' : 2, 'Valor4' : 3, 'Valor5' : 'café',
'Valor6' : 'banana', 'Valor7' : 'mulher', 'Valor8' : 'colher','Valor9' : 'alvo', 'Valor10' :1,
'Valor11' : 2, 'Valor12' : 3, 'Valor13' : 'olá'}

print("Resultado:", dicio['Valor13'])

print("*****QUESTAO 6 *****")
print("dicionario é uma forma de localizar strings por meio de indices. Tupla é uma lista que armazena strings")

print("*****QUESTAO 7 *****")
email ='user@domain.com'
dicionario = {'valor1' : 'user', 'valor2': '@', 'valor3' : 'domain.com'} 
print("Resultado:", dicionario['valor3'])

print("*****QUESTAO 8 *****")
olhar = 'Existe um cachorro ai?'
busca = 'cachorro'

if busca in olhar:
    print("true")
else:
    print("False")

print("***** PROBLEMA FINAL *****")
def capturar_velocidade(speed):
    speed = input("Velocidade:")
    if speed <= 60:
        print("Sem multa.")



