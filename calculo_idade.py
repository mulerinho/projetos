# Calculo de idade usando biblioteca datetime
import datetime
from datetime import date
# Criando inputs separados para capturar data.
dia = int(input('Qual o dia do seu nascimento: '))
mes = int(input('Qual o mês do seu nascimento: '))
ano = int(input('Qual o ano do seu nascimento: '))
# Criando uma sting com os dados para poder manipular.
datanasc = datetime.date(ano, mes, dia)
diferenca = (date.today() - datanasc)
# Calculando resultadi
result = (diferenca.days / 365)
print(f'A sua idade é : {result:.0f} anos')
