# Exercicio com array e numpay para mostras maior e menor numeros digitados e seus indices.
lista = []
lista1 = []
maximo = 0
minimo = 0
import numpy as np
for count in range(0, 5):
    num = int(input('Digite um numero: '))
    lista.append(num)
    maximo = max(lista)
    minimo = min(lista)
    lista1 = lista
    lista1 = np.array(lista1)
    indices = np.where(lista1 == maximo)
    indices1 = np.where(lista1 == minimo)
print('==//=='* 25)
print(f'Você digitou os seguintes números: {lista}')
print()
print(f'f O maior número foi o {maximo} e seu índice e ou índices : {indices} ')
print(f'f O menor número foi o {minimo} e seu índice e ou índices : {indices1} ')




