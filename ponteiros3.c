#include <stdio.h>
int funcComRetono(int y);
void semretorno(int y);
void ponteiro(int *y);
void main(){

    int x = 10;
    int resultado;
    printf("Valor antes da função com retorno e fora da mesma %d: \n", x);
    printf("++++++++++++++++++++++++++++++++++++++++++++++ \n");

    // Chamada da função
    x = funcComRetorno(x);
    semretorno(x);
    // Chamada depois da função.
    printf("Valor depois da funcao com retorno  na main() %d: \n", x);
    printf("++++++++++++++++++++++++++++++++++++++++++++++ \n");
    ponteiro(&x);
    printf("##############################################\n\n");
    printf("Valor de x na main() Depois do Ponteiro. %d:\n", x);
    printf("\n\n");
}

int funcComRetorno(int y){
    y = y + 15;
    printf("Valor dentro da função com retorno %d\n", y);
    printf("++++++++++++++++++++++++++++++++++++++++++++++ \n");
    return y;
}

// funcao sem retorno.
void semretorno(int y){
    y = ++y;
    printf("Valor da funcao void sem retorno Valor dentro da funcao: %d\n", y);
    printf("-----------------------------------------\n");
}

void ponteiro(int *y){
    *y = *y + 11;
    printf("Valor com Ponteiros: %d\n", *y);

}
