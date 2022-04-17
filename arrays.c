//Exercicio com arrays e funções.
//Protótipo de função
void name();
void somando();
//Variaveis Globais.
char nome[10];
float nota[3];
float media = 0;
int soma = 0;
int i= 0;
int main(){
    //Capturando Dados.

    name();
    for (i=0;i<3;i++){
    printf("Digite a nota do aluno: \n");
    scanf("%f", &nota[i]);}


    for (i=0;i<3;i++){
    printf("A nota do %s\n  é %.2f \n",nome, nota[i]);
    somando();
    mediaNotas();
    printf("\nA soma das notas do aluno %s é %d\n",nome,soma);
    printf("Sua média é:%.2f\n", media);

    }

return 0;
}
//Criando funções.
void name(){
    printf("Digite o nome do aluno:\n");
    gets(nome);
    return 0;
}

void somando(){
    soma = nota[i] + soma;
    return 0;
}

void mediaNotas(){
    media = soma /3;
    return 0;

}

