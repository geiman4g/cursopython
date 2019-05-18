x = input("Digite un numero x para compararlo con 30: ")
if int(x) < 30: 
    print("x  es menor que 30")
elif int(x) == 30:
        print("x es igual 30")
else:
    print("x es mayor que 30")


y = input("Digite un numero y para verificar si esta entre 2 y 100: ")

if int(y) > 2 and int(y) <= 100: 
    print("y  esta en el rango de 100")
else:
    print("y no esta en el rango 2 a 100")