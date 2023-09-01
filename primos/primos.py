# coding: latin-1

# Função que calcula todos os números primos até o número N de forma linear
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

# Função que calcula todos os números primos até o número N de forma recursiva
def p_recursivo(N):
    # código
    return 1

# Trata input para receber apenas números maiores que 1
while True:
    try:
        N = int(input("Informe um número maior que 1: "))

    except:
        continue
    
    if N > 1:
        break

print("\n")
print("p_linear({}) = {}".format(N, p_linear(N))) # Imprime todos os números primos até o número N através da função linear
print("p_recursivo({}) = {}".format(N, p_recursivo(N))) # Imprime todos os números primos até o número N através da função recursiva
print("\n")
