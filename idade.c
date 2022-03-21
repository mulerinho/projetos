// extrutura de decisão if, else if, else.
#include <stdio.h>
void main(){
// Declarando variaveis.
char nome;
int idade;
    printf("Digite sua idade: ");
    scanf("%d", &idade);

    if(idade < 18){
    printf("Voçê é menor de idade.");

    }else if(idade > 18 && idade < 60){
    printf("Você é adulto.");

    }else{
    printf("Você é idoso.");

    }

    printf("\n Sua idade  é: %d ", idade);
}
