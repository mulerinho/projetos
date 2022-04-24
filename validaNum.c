// Exercício para validar nmeros inteiros ou reais em C.
#include <stdio.h>
// Variaveis Globais.
    float num = 0;
    int inteiro = 0;
    int soma = 0;
    float real = 0;
    float somareal = 0;
int main(){
// Capturando dados.
    for (int i = 0; i < 4; i++){
    printf("Digite um numero :");
    scanf("%f", &num);
    // Processando e apresentando resultados.
    if (num == (int)num){
        inteiro = num;
        soma = inteiro + soma;
        printf("O %d é um número inteiro.\n", inteiro);
        printf("A soma dos números inteiros : %d\n", soma);}
    else {
        printf("O %.2f é um número real.\n", num);
        somareal = num + somareal;
        printf("A soma dos números reais : %.2f\n", somareal);}

    }

return 0;}

