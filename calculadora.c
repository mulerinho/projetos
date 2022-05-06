// Calculadora com função.
#include <stdio.h>
    // Protótipo de função.
    void soma(void);
    void sub(void);
    void mult(void);
    void div(void);
    // Declarandovariáveis globais.
    int a = 0;
    int b = 0;

    void main(){
        // Varivel local
        int valor;
    // Coletando dados.
    printf("Digite um número: \n");
    scanf("%d", &a);
    printf("Digite um segundo número: \n");
    scanf("%d", &b);
    // Switch case.
    printf("Digite:\n 1-Soma: \n 2-Subtração: \n 3-Multiplicação: \n 4-Divisão: \n\n");
    scanf("%d", &valor);

    switch (valor){
    case 1:
        soma();
        break;
    case 2:
        sub();
        break;
    case 3:
        mult();
        break;
    case 4:
       div();
       break;
    default:
        printf("Opção invalida!");

    }

    return 0;
    }

    void soma(void){

       int soma;
       soma = a+b;
       printf("O valor da soma de \"A = %d\" + \"B = %d\" é: %d", a,b,soma);}


   void sub(void) {
       int sub;
       sub = a - b;
       printf("O valor da subtração de \"A = %d\" - \"B = %d\" é: %d", a,b,sub);}


   void mult(void){

        int mult = 0;
        mult = a * b;
        printf("O valor da multiplicação de \"A = %d\" * \"B = %d\" é: %d", a,b,mult);}

     void div(void){

        int div = 0;

        div = a / b;
        printf("O valor da divisão de \"A = %d\" / \"B = %d\" é: %d\n", a,b,div);

   }

