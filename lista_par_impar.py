# CRIAR UMA ÚNICA LISTA QUE RECEBA 7 NÚMEROS, PARES E ÍMPARES E SEPARE EM DUAS LISTAS DENTRO DELA.
lista_par = []
lista_impar = []
lista =[]
valor = 0

for i in range(1, 8):
      valor = int(input(f'Digite um valor para posição {i}: '))
      if (valor%2) == 0:
          lista_par.append(valor)
      else:
          lista_impar.append(valor)
lista.append(sorted(lista_par[:]))
lista.append(sorted(lista_impar[:]))
lista_par.clear()
lista_impar.clear()



print('='* 45)
print(f'Os némeros pares são:  {lista[0][0:]}')
print(f'Os números ímpares são: {lista[1][0:]}')
print(lista)