# Exercicio criando uma função para calculo percentual.
def percentual(x1, x2):
    return  (x1 + (x1 * x2 / 100))

x1 = int(input('Digite um número: '))
x2 = int(input('Digite um valor para porcentagem: '))

print(f'O valor digitado com a soma da porcentagem é {percentual(x1,x2)}')