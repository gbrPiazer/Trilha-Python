name= 'Gabriel'
age = 21
profissao = 'NOC'

#Old Style %

print("Olá, chamo %s.Eu tenho %i anos de idade e trabalho como %s"%(name, age, profissao))

#Format {}

print("Olá, chamo {}.Eu tenho {} anos de idade e trabalho como {}.".format(name, age, profissao))
print("Olá, chamo {2}.Eu tenho {1} anos de idade e trabalho como {0}.".format(profissao, age, name))
print("Olá, chamo {nome}.Eu tenho {idade} anos de idade e trabalho como {profissao}.".format(nome = name, idade = age, profissao = profissao))

#f-string

print(f"Olá, chamo {name}.Eu tenho {age} anos de idade e trabalho como {profissao}.")


##Formatação com f-string

PI = 3.14159

print(f"Valor de PI: {PI}")
print(f"Valor de PI: {PI: .2F}")
print(f"Valor de PI: {PI: 10.2F}")