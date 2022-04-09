# Exercicio Listas maior peso.
# Declarando
contador = 0
lista = []
lista1 = []
continuar = 'S'
# Capturando dados
while continuar == 'S':
    nome = str(input('Digite o seu nome: '))
    contador += 1
    peso = float(input(('Digite o seu peso: ')))
    lista.append(peso)
    lista.append(nome)
    lista1.append(lista[:])
    lista.clear()
    nova = sorted(lista1)


# Validando pergunta

    while True:
        continuar = str(input('Deseja continuar? S/N')).upper()

        if continuar == 'N':
            print('Fim do programa.')
            break
        elif continuar == 'S':
            break
        if continuar != 'S' and continuar != 'N':
            print('Digite somente S/N.')

print('='*50)
print(f'O número de pessoas cadastradas: {contador}')
print(f'Os dois menores pesos são: {nova[0][1]} com {nova[0][0]} kilos. e {nova[1][1]} com {nova[1][0]}.')
print(f'Os dois maiores pesos são: {nova[-1][1]} com {nova[-1][-0]} kilos. e {nova[-2][1]} com {nova[-2][0]}.')
print(nova)
