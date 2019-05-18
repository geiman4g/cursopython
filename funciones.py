def hola(w,z):
    while int(w) <= int(z):
        print(w)
        w = int(w) + 1
def suma(a,b):
    return a + b

w = input("Digite el contador comienza en: ")
z = input("Digite el contador termina en: ")
hola(w,z)
print("la suma es: " + str(suma(7,9)))