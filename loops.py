lista = ['manzanas','peras','naranjas','limones']

for lista in lista:
    if lista == 'peras':
        print('hay que comprar agua')
        break
    print(lista)



for lista in lista:
    if lista == 'peras':
        print('hay que comprar agua')
        continue
    print(lista)

for y in range(1,5):
    print(y)


w = input("Digite el contador comienza en: ")
z = input("Digite el contador termina en: ")
while int(w) <= int(z):
    print(w)
    w = int(w) + 1
