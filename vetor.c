#include <stdio.h>
#include <stdlib.h>
// Recebendo dados, armazenando em um vetor e apresentando a soma.s
int main(){
int i,soma,num,soma_vetor, v[4];

    for (i = 1;i < 4; i++){
    printf("Digite um valor para num: \n");
    scanf("%d", &v[i]);
    soma = v[1] + v[2] + v[3];
    printf("O vetor recebeu: %d \n", v[i]);
    }

printf("O valor da soma total do vetor é: %d\n", soma);
return 0;
}
