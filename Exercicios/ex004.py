var = input('Digite algo: ')
print('A classe primitiva desse valor é {}'.format(type(var)))
print('Só tem espaços? {}'.format(var.isspace()))
print('É um número? {}'.format(var.isnumeric()))
print('É alfabetico? {}'.format(var.isalpha()))
print('É alfanúmerico? {}'.format(var.isalnum()))
print('Está em maiúsculo? {}'.format(var.isupper()))
print('Está em minúsculo? {}'.format(var.islower()))
print('Está capitalizada? {}'.format(var.capitalize()))