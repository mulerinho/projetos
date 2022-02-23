# Validação de CPF, exercicio revisado.
soma = 0
soma2 = 0
calc = 0
calc2 = 0
lista1 = []
lista2 = []
cpf = input('Digite o CPF sem pontos ou barra : ')
lista1.extend(cpf[0:9])
lista2.extend(cpf[0:11])
# Capturando dados.
for c, d in enumerate(range(10, 0, -1)):
    soma += int(cpf[c]) * d
# Capturando dados para segundo digito.
for e, f in enumerate(range(11, 1, -1)):
    soma2 += int(cpf[e]) * f
# calculo primeiro digito
calc = 11 - (soma % 11)
if calc > 9:
    calc = 0
# Soma para o segundo digito.
calc2 = 11 - (soma2 % 11)
if calc2 < 9:
    lista1.append(str(calc))
    lista1.append(str(calc2))
# Comparando os dados e validando
if lista1 == lista2:
    print('CPF válido!')
else:
    print('CPF inválido!')








