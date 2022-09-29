from random import randint, random

moneda=randint (1, 2)
print("1.cara")
print("2.sello")
eleccion= input ("elije cara o sello:")


if moneda == eleccion: 
    print("Ganaste")

elif moneda!=eleccion:
    print('perdiste, sigue intentando')

else:
    print("caracteres no permitidos")