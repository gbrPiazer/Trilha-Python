

MAIOR_IDADE = 18
IDADE_AULA = 16

idade = int(input("Informe sua idade: "))

print("1")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade< MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

print("2")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH")

print("3")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH")

print("4")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade >= IDADE_AULA:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas")
else:
    print("Ainda não pode tirar a CNH")

