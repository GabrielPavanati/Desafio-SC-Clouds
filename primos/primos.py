# coding: latin-1

# Função que calcula todos os números primos até o número N de forma linear
def p_linear(N, seq_primos=[]):
    
    for num in range(2, N + 1):
        if all(num % primo != 0 for primo in seq_primos):
            seq_primos.append(num)
        
    return seq_primos

# Função que calcula todos os números primos até o número N de forma recursiva
def p_recursivo(N, num=2, seq_primos=[]):
    if num > N:
        return seq_primos
    
    if all(num % primo != 0 for primo in seq_primos):
        seq_primos.append(num)
    
    return p_recursivo(N, num + 1, seq_primos)

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
