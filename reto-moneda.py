from random import randint, random

moneda=randint (1, 2)

if moneda==1:
   resultado='cara'
if moneda==2:
    resultado='sello'
  
eleccion= input ("elije cara o sello:")

if eleccion == resultado: 
    print("Ganaste")

else:
    print('perdiste, sigue intentando')