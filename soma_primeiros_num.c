//O programa deve somar os 5 primeiros números digitados e apresentar o valor da soma dos mesmos.
#include <stdio.h>
int main(){
    //Declarando variaveis:
    int num;
    int soma = 0;
    int count = 0;
    while (num != 0){
        //Coletando Dados:
        printf("Digite um valor para Numero ou tecle [0] para sair: \n");
        scanf("%d", &num);
        count = count +1;
        //Processando condicionais.
        if (count <=5){
            soma = soma + num;
        //Apresentando resultados
            printf("Número do contador => %d\n", count);
            printf("O valor da soma até o quinto número: %d\n", soma);}
        else if (count > 5){
            printf("\n Soma encerrada.\n");

            }






    }








return 0;
}
