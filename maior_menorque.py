# Ler cinco valores e mostra o menor e o maior valor digitado.
maior = 0
menor = 0
for num in range(1, 6):
    peso = float(input(f'Digite o seu peso: '))
    if num == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('='* 50)
print(f' O Menor é de {menor}')
print(f' O Maior é de {maior}')