# coding: latin-1

# Trata input para receber apenas números maiores que 1
while True:
    try:
        N = int(input("Informe um número maior que 1: "))

    except:
        continue
    
    if N > 1:
        break

print("p_linear({}) = {}".format(N, p_linear(N))) # Imprime todos os números primos até o número N através da função linear
print("p_recursivo({}) = {}".format(N, p_recursivo(N))) # Imprime todos os números primos até o número N através da função recursiva

# Função que calcula todos os números primos até o número N de forma linear
def p_linear(N):
    # código
    return

# Função que calcula todos os números primos até o número N de forma recursiva
def p_recursivo(N):
    # código
    return
