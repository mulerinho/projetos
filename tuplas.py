# Exercicio em tuplas.
index = 0
sair = ''
tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre " 0 e 20 ": '))
    print()
    if numero < 0 or numero > 20:
        numero = int(input('Digite apenas numeros entre " 0 e 20 ": '))
    if numero < 0 or numero > 20:
        sair = input('Digite "s" para sair ou ENTER para continuar. ').upper()
        if sair == 'S':
            print('Fim')
            break
    elif numero >= 0 or numero <= 20:
        index = numero
        print('='* 50)
        print(f'O numero digitado foi {tupla[index]}')
        print('='*50)
    
        
        
        
        

        
        
    
    
    
    

#index = numero
#print(tupla[index])