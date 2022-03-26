#include <stdio.h>
void main(){
//Prgrama para criar uma sequencia de números crescente ou decrescente, conforme entrada.
//Declarando variaveis.
int a, b, ordenacao, controle;
// Entrada de dados.
printf("Digite um número para A: ");
scanf("%d", &a);
printf("Digite um número para B: ");
scanf("%d", &b);

if (a <= b)
    ordenacao = 1;
else
    ordenacao = -1;

for(controle = a; controle != b + ordenacao; controle = controle + ordenacao){

    printf("%d", controle);

}





}
