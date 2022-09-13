

from random import randint


descuento=randint(1, 4)
'''1. bola azul 2.bola blanca 3. bola blanca 4.bola roja'''
print('Supermercado Noe')
Compra =int(input('ingrese el valor total de su compra:'))
if Compra>50000:
    print('felicidades puede acceder al descuento')
    input('Elija un numero entre el 1 y 4:')
    if descuento==1:
        opcion1= 1-(30/100)*(Compra)
        print('Felicidades, tiene un 30% de descuento en su compra')
        print('su valor de descuento es', opcion1)
    elif descuento==2:
        print('Hoy es tu dia de suerte, te llevas tu compra totalmente gratis')
    elif descuento==3:
        opcion3=1-(50/100)*(Compra)
        print('felicidades, tiene un descuento de 50% de descuento en su compra ')
        print('su valor de descuento es', opcion3)
    elif descuento==4:
        opcion4=1-(10/100)*(Compra)
        print('Felicidades, tiene un 10% de descuento en su compra')
        print('su valor de descuento es', opcion4)

