#include <stdio.h>

int main(){
    //Declarando variáveis.
    int l = 0;
    int c = 0;
    int m[3][3];

//Capturando dados:
    for (l=0;l<3;l++){
        for (c=0;c<3;c++){
            printf("Digite valor para posição [%d][%d]: \n",l,c);
            scanf("%d", &m[l][c]);}

    }
    printf("=================================\n");
    //Apresentando matriz.
    for (l=0;l<3;l++){
        for (c=0;c<3;c++){
            printf("%8d", m[l][c]);
        }
        printf("\n");
    }

return 0;
}
