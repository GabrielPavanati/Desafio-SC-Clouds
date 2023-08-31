#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "pt_BR.UTF-8");

    int N;
    
    while (1)
    {
        printf("Informe um número não negativo: ");
        scanf_s("%d", &N);

        if (N >= 0)
        {
            break;
        }
    }

    printf("\n fib(%d) = %d \n", N, fib_linear(N));
    printf("\n fib(%d) = %d \n", N, fib_recursivo(N));
}

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

int fib_recursivo(int N)
{
    if (N == 0) return 0;
    else if (N == 1) return 1;
    else
    {
        return fib_recursivo(N - 1) + fib_recursivo(N - 2);
    }
}