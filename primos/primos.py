# coding: latin-1

# Trata input para receber apenas n�meros maiores que 1
while True:
    try:
        print("Informe um n�mero maior que 1: ")
        N = int(input())

    except:
        continue
    
    if N > 1:
        break
