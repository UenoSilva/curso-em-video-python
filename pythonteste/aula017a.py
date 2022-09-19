num = [2, 5, 9, 1]
num[2] = 4
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 3 in num:
    num.remove(6)
else:
    print('Não achei o númerumo 3')
print(num)
print(f'Essa lista tem tantos {len(num)} elementos')
