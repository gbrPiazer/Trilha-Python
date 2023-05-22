name = 'gAbriEL'

print("Maiúscula, minúscula e título")

print(name)
print(name.upper())
print(name.lower())
print(name.title())

name = '      Gabriel   ' 

print("Eliminando espaços em branco")

print(name + '.')
print(name.strip() + '.')
print(name.lstrip() + '.')
print(name.rstrip() + '.')

print("Junções e centralizações")

name = ' Menu '

print(name)
print(name.center(20, '#'))
print(".".join(name))
