# coding: latin-1

# Trata input para receber apenas n�meros maiores que 1
while True:
    try:
        N = int(input("Informe um n�mero maior que 1: "))

    except:
        continue
    
    if N > 1:
        break

print("p_linear({}) = {}".format(N, p_linear(N))) # Imprime todos os n�meros primos at� o n�mero N atrav�s da fun��o linear
print("p_recursivo({}) = {}".format(N, p_recursivo(N))) # Imprime todos os n�meros primos at� o n�mero N atrav�s da fun��o recursiva

# Fun��o que calcula todos os n�meros primos at� o n�mero N de forma linear
def p_linear(N):
    # c�digo
    return

# Fun��o que calcula todos os n�meros primos at� o n�mero N de forma recursiva
def p_recursivo(N):
    # c�digo
    return
