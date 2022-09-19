valores = list()
for i in range(0, 5):
    valores.append(int(input('Digite um número: ')))
for n in range(0, 5):
    p = valores[n]
    valores.insert(p, valores[n])
    valores.pop(n)

print(valores)
