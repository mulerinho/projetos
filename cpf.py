l11 = [] # Anexa 11 digits do cpf
l7 = []  # Anexa 7 digitos do cpf
list7 = []
list11 = []
soma = 0
soma2 = 0
calc = 0
calc2 = 0
cpf = input('Digite o CPF sem pontos ou barra : ')
# Capturando dados.
for c in range(1, 10):
    l7.append(int(cpf[0]))
    l7.append(int(cpf[1]))
    l7.append(int(cpf[2]))
    l7.append(int(cpf[3]))
    l7.append(int(cpf[4]))
    l7.append(int(cpf[5]))
    l7.append(int(cpf[6]))
    l7.append(int(cpf[7]))
    l7.append(int(cpf[8]))

for d in range(0, 12):
    l11.append(int(cpf[0]))
    l11.append(int(cpf[1]))
    l11.append(int(cpf[2]))
    l11.append(int(cpf[3]))
    l11.append(int(cpf[4]))
    l11.append(int(cpf[5]))
    l11.append(int(cpf[6]))
    l11.append(int(cpf[7]))
    l11.append(int(cpf[8]))
    l11.append(int(cpf[9]))
    l11.append(int(cpf[10]))
# Definindo tamanho das listas para comparação depois da validação.
list7.extend(l7[0:9])
list11.extend(l11[0:11])
# Somando listas
soma = (l7[0] * 10 + l7[1] * 9 + l7[2] * 8 + l7[3] * 7 + l7[4] * 6 + l7[5] * 5 + l7[6] * 4 +
l7[7] * 3 + l7[8] * 2 )
# calculo primeiro digito
calc = 11 - (soma % 11)
if calc > 9:
    calc = 0
# Soma para o segundo digito.
soma2 = (
    l7[0] * 11 +
    l7[1] * 10 +
    l7[2] * 9 +
    l7[3] * 8 +
    l7[4] * 7 +
    l7[5] * 6 +
    l7[6] * 5 +
    l7[7] * 4 +
    l7[8] * 3 +
    calc * 2)
# calculo segundo digito.
calc2 = 11 - (soma2 % 11)
list7.extend([calc, calc2])
if list7 == list11:
    print(f'O seu CPF foi validado com sucesso! {cpf}')
else:
    print('CPF invalido!')



