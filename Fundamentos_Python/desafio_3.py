n = int(input())

while(n > 0):
    N = str(input(''))
    numeros_separados = N.split(" ", maxsplit=1)
    total_list = len(numeros_separados)
    A = int(numeros_separados[0])
    print(A)
    if total_list == 2:    
        B = int(numeros_separados[1])
        if A <= 1000:
            print('encaixa')
            if B <= 1000:
                print('encaixa')
                continue
            else:
                print('nao encaixa')
                continue
        else:
            print('nao encaixa')
            if B <= 1000:
                print('encaixa')
                continue
            else:
                print('nao encaixa')
                continue
    else:
        A = int(numeros_separados[0])
        if A <= 1000:
            print('encaixa')
            continue
        else:
            print('nao encaixa')
            continue

    



