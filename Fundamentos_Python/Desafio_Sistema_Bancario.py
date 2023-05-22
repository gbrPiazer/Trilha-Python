menu = '''
#############################

        [0] Depositar
        [1] Sacar
        [2] Extrato
        [3] Sair

#############################
'''

saldo = 0
limite = 500
extrato = ''
saque = ''
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == '0':
        valor = float(input("Qual valor deseja depositar?"))

        print(valor)
        if valor >= 30:
            saldo += float(valor)
            extrato += f'+ R$ {valor:.2f} \n'
            print(f'Depósito de R$ {valor} concluído com sucesso, seu saldo atual é R$ {saldo}')
        else:
            print('O valor mínimo para depósito é R$ 30')

    elif opcao == '1':
        if LIMITE_SAQUE < 0:
                print('Limite de saques atingido')
        else:
            saque = float(input('Qual valor desejar sacar?'))

            if saque <= saldo:
                if saque <= limite:
                    LIMITE_SAQUE -= 1
                    saldo -= saque
                    extrato += f'- R$ {saque:.2f} \n'
                    print(f'Retire seu dinheiro, saque realizado com sucesso seu saldo atual é R$ {saldo}')
                else:
                    print('Seu limite de saque diário é de R$ 500')
            else:
                print('Saldo indisponível.')
                
    elif opcao == '2':
        if saldo > 0:
            print('\n=============== EXTRATO ===============')
            print(extrato)
            print(f'Saldo total R$ {saldo}')
            print('\n=======================================')
        else:
            print('\n=============== Extrato ===============')
            print('Não foram realizadas movimentações.')
            print('\n=======================================')

    elif opcao == '3':
        break

    else:
        print('Operação inválida, por favor selecione novamente')