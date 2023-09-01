# coding: latin-1

# Fun��o que calcula todos os n�meros primos at� o n�mero N de forma linear
def p_linear(N):
    memoria = []
    
    for i in range(2, N + 1):
                
        num_divisiveis = 0

        for j in range(1, N + 1):
            if i % j == 0:
                num_divisiveis += 1
                
        if num_divisiveis == 2:
            memoria.append(i)
            
    return memoria

seq_recursiva = []

# Fun��o que calcula todos os n�meros primos at� o n�mero N de forma recursiva
def p_recursivo(N):
    # c�digo
    return 1

# Trata input para receber apenas n�meros maiores que 1
while True:
    try:
        N = int(input("Informe um n�mero maior que 1: "))

    except:
        continue
    
    if N > 1:
        break

print("\n")
print("p_linear({}) = {}".format(N, p_linear(N))) # Imprime todos os n�meros primos at� o n�mero N atrav�s da fun��o linear
print("p_recursivo({}) = {}".format(N, p_recursivo(N))) # Imprime todos os n�meros primos at� o n�mero N atrav�s da fun��o recursiva
print("\n")
