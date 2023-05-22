conta_normal = True
conta_universitaria = False


saldo = 2000
SAQUE = 0
SAQUE = float(input('Qual valor deseja sacar?'))
cheque_especial = 450

if conta_normal:
    if saldo >= SAQUE:
        print("Saque realizado com sucesso!")
    elif SAQUE <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente")
elif conta_universitaria:
    if saldo >= SAQUE:
        print("Saque realizado com sucesso!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente")
else:
    print("Sistema não reconheceu o tipo de conta, entre em contato com seu gerente")