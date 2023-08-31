#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "pt_BR.UTF-8"); // Função que permite a exibição de caracteres acentuados

    int N;
    
    // Trata input para receber apenas número não negativo
    while (1)
    {
        printf("Informe um número não negativo: ");
        scanf_s("%d", &N);

        if (N >= 0)
        {
            break;
        }
    }

    printf("\n fib_linear(%d) = %d \n", N, fib_linear(N)); // Imprime o N-ésimo termo usando a função linear
    printf("\n fib_recursivo(%d) = %d \n", N, fib_recursivo(N)); // Imprime o N-ésimo termo usando a função recursiva
}

// Função para calcular o N-ésimo termo da sequência de Fibonacci de forma linear
int fib_linear(int N)
{
    int memoria[3];

    if (N == 0) return 0;
    else if (N == 1) return 1;
    else
    {
        for (int i = 0; i <= N; i++)
        {
            if (i == 0)
            {
                memoria[0] = 0;
            }
            else if (i == 1)
            {
                memoria[1] = 1;
            }
            else
            {
                memoria[2] = memoria[1] + memoria[0];
                memoria[0] = memoria[1];
                memoria[1] = memoria[2];
            }
        }
        return memoria[2];
    }
}

// Função para calcular o N-ésimo termo da sequência de Fibonacci de forma recursiva
int fib_recursivo(int N)
{
    if (N == 0) return 0;
    else if (N == 1) return 1;
    else
    {
        return fib_recursivo(N - 1) + fib_recursivo(N - 2);
    }
}