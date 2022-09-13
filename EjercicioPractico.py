
CantidadP=int(input('ingrese la cantidad de productos que va a llevar:'))
Valorpaga= int(input('Con que valor cancela la cuenta:'))
ValorP= 10000
Total= CantidadP * ValorP
Cambio= Total-Valorpaga

print(f'el total de su compra es {Total}')
print(f'su cambio es {Cambio}')
