# reentrada de dados unis
lista = []
nota = 0
nota1 = 0
nota2 = 0
media = 0
soma = 0
media = 0
pergunta = ''
nome = input('Digite o nome do aluno: ')
while True:
    nota = int(input('Digite a primeira nota do aluno: '))
    if nota < 25:
        print(f'O valor da nota foi: {nota},')
    else:
        print('Voçe deve inserir a primeira nota abaixo de 25.')
        continue
    print('=/='* 15)
    pergunta = input('Deseja inserir a próxima nota do aluno?\n "S" para Sim ou "ENTER" para repetir.').upper()
    if pergunta == 'S':
        lista.append(nota)

    while True:
        print('=/='*15)
        nota1 = int(input('Digite a segunda nota do aluno: '))
        if nota1 >= 30 and nota1 <= 35:
            print(f'A nota digitada foi: {nota1}')
            break
        else:
            print('O valor da segunda nota deve estar entre 30 e 35, digite novamente.')
            print()
    pergunta = input('Deseja inserir a próxima nota do aluno?\n "S" para Sim ou "ENTER" para repetir.').upper()
    if pergunta == 'S':
        lista.append(nota1)
    while True:
        nota2 = int(input('Digite a terceira nota, deve estar entre 36 e 40: '))
        if nota2 > 35 and nota2 <= 40:
            lista.append(nota2)
            break

        else:
            continue
    break




soma = sum(lista)
media = soma / 3
print('=/='* 15)
print(f'A soma das notas do aluno {nome}, foi: {soma} ')
print()
print(f'A média do aluno {nome} foi {media:.2f}')





