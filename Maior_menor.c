#include <stdio.h>
int main(){
// Declarando variaveis.
int num;
int maior = 0;
int menor = 0;
// Vriando laço
for (int c = 0; c < 10 ; c++){
// Coletendo dados.
printf("Digite num: ");
scanf("%d", &num);

// Pocessando maior e menor valor digitados
if (c == 0){maior = num; menor = num;}
else if (num > maior){maior = num;}
else if (num < menor){menor = num;}

}
// Apresentando resultado.
printf("O Maior é %d\n", maior);
printf("O Menor é %d\n", menor);


return 0;
}
