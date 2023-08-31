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

        break;

        if (N >= 0)
        {
            break;
        }
    }

    printf("\n fib(%d) = %d \n", N, fib(N));
}

int fib(int N)
{
    return N;
}